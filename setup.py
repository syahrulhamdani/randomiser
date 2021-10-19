from setuptools import setup, find_packages


with open("README.md", "r") as f:
    long_desc = f.read()

setup(
    name="randomizer",
    version="0.0.1",
    description="Random data generator",
    url="https://github.com/syahrulhamdani/randomiser",
    author="Syahrul Hamdani",
    author_email="syahrulhamdani.ds@gmail.com",
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_desc,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests ~= 2.26.0",
    ],
    extras_require={
        "dev": [
            "pytest~=6.2.5",
        ],
    },
)
