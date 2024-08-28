
from common.exception.MyCustomError import *

try:
    print("try begin")
    raise MyCustomError("사용자 예외가 발생했습니다.")
    print("try end")
except MyCustomError as e:
    print(f"except MyCustomError => {e}")
except Exception as e:
    print(f"except Exception {e}")
finally:
    print("finally")
