from setuptools import setup, find_packages

setup(
    name="env-dev-prod",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "": ["*.py", "*.txt", "*.yaml", "*.json"],  # 필요한 파일 확장자 추가
    },
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        # 의존성 목록
    ],
    entry_points={
        'console_scripts': [
            'myapp=my_app.main:run',
        ],
    },
)