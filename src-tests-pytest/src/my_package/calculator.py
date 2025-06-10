"""
간단한 계산기 모듈
"""


def add(a: float, b: float) -> float:
    """두 수를 더합니다."""
    return a + b


def subtract(a: float, b: float) -> float:
    """두 수를 뺍니다."""
    return a - b


def multiply(a: float, b: float) -> float:
    """두 수를 곱합니다."""
    return a * b


def divide(a: float, b: float) -> float:
    """두 수를 나눕니다.
    
    Args:
        a: 분자
        b: 분모 (0이 아니어야 함)
        
    Returns:
        float: 나눈 결과
        
    Raises:
        ValueError: b가 0인 경우
    """
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b
