from setuptools import setup, find_packages

setup(
    name="your-package-name",
    version="0.1.0",
    description="설명 예시",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "python-dotenv",
        "loguru"
    ],
    extras_require={
        "dev": ["pytest", "black", "flake8", "mypy"]
    },
    python_requires=">=3.8",
)
