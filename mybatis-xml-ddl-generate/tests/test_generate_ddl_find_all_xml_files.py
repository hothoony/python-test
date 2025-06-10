import pytest
from my_package.generate_ddl import find_all_xml_files

def test_find_all_xml_files():
    result = find_all_xml_files("/Volumes/mydata/office_work/project/ploonet_total/project_src/ploonet-total-backend/src/main/java/com/ploonet/total/backend/mapper")
    print(len(result))
    assert True is True
