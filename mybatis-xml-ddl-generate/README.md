## mybatis 의 xml 파일로 부터 ddl 추출하기

### 실행하기
```shell
XML_DIR=/Volumes/mydata/office_work/project/ploonet_total/project_src/ploonet-total-backend/src/main/resources/mapper && \
python3 src/my_package/generate_ddl.py $XML_DIR
```

### 결과
out/ddl_output.sql
