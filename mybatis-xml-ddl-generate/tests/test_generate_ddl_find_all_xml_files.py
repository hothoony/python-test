import pytest
from my_app.generate_ddl import find_all_xml_files

def test_find_all_xml_files():
    print()
    # result = find_all_xml_files("/Volumes/mydata/office_work/project/ploonet_total/project_src/ploonet-total-backend/src/main/resources/mapper")
    result = find_all_xml_files("/Volumes/mydata/office_work/JLS/workspace_All_modify/workspace_BMS/bms-global/src/main/resources/mybatis/mapper/oracle")
    print('result=',len(result))
    assert True is True
