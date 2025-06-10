import os
import xml.etree.ElementTree as ET
import sqlparse
import re
from collections import defaultdict

def find_all_xml_files(root_dir):
    xml_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".xml"):
                xml_files.append(os.path.join(dirpath, filename))
    return xml_files

def extract_sql_from_mapper(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        sql_statements = []

        for elem in root.findall(".//*"):
            if elem.tag in ["select", "insert", "update", "delete"]:
                sql = ''.join(elem.itertext()).strip()
                if sql:
                    sql_statements.append(sql)
        return sql_statements
    except Exception as e:
        print(f"[!] XML 파싱 실패: {file_path} - {e}")
        return []

def extract_tables_and_columns(sql_list):
    table_columns = defaultdict(set)
    for sql in sql_list:
        parsed = sqlparse.format(sql, strip_comments=True, reindent=True)
        # FROM, INTO 등에서 테이블 추출
        tables = re.findall(r'(?:from|into|update)\s+([a-zA-Z_][a-zA-Z0-9_]*)', parsed, re.IGNORECASE)
        # SELECT 컬럼 추출
        cols = re.findall(r'select\s+(.*?)\s+from', parsed, re.IGNORECASE | re.DOTALL)

        if tables:
            table = tables[0]
            if cols:
                column_list = cols[0].split(',')
                for col in column_list:
                    name = col.strip().split()[-1].strip("`")
                    table_columns[table].add(name)
            else:
                # INSERT, UPDATE 등일 경우 VALUES 절에서 추출 가능
                matches = re.findall(r'\((.*?)\)', parsed)
                if matches:
                    for match in matches:
                        column_list = match.split(',')
                        for col in column_list:
                            col_name = col.strip().split()[-1].strip("`")
                            table_columns[table].add(col_name)
    return table_columns

def generate_ddl(table_columns):
    ddl_list = []
    for table, columns in table_columns.items():
        lines = [f"  {col} VARCHAR(255)" for col in sorted(columns)]
        ddl = f"CREATE TABLE {table} (\n" + ",\n".join(lines) + "\n);"
        ddl_list.append(ddl)
    return ddl_list

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("사용법: python3 generate_ddl_all.py <mapper 디렉토리 경로>")
        sys.exit(1)

    root_dir = sys.argv[1]
    all_sql = []

    print(f"[+] 디렉토리 검색 중: {root_dir}")
    xml_files = find_all_xml_files(root_dir)

    print(f"[+] XML 파일 {len(xml_files)}개 발견")

    for file in xml_files:
        sqls = extract_sql_from_mapper(file)
        if sqls:
            all_sql.extend(sqls)

    print(f"[+] SQL 구문 {len(all_sql)}개 추출 완료")

    table_columns = extract_tables_and_columns(all_sql)
    ddl_output = generate_ddl(table_columns)

    print("\n📦 생성된 DDL 목록:")
    for ddl in ddl_output:
        print(ddl)
        print()
