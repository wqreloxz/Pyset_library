from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pyset-sorting",
    version="1.0.0",
    description="library for sorting objects into sets based on parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="wqreloxzz",
    author_email="your.wqreloxzz@gmail.com",
    url="https://github.com/wqreloxz/Pyset_library",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "pyset=pyset.cli:main",
        ],
    },
)
