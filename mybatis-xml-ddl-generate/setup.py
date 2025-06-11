from setuptools import setup, find_packages

setup(
    name="my_app",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6",
    install_requires=[
        # 여기에 필요한 패키지들을 추가하세요
    ],
)
