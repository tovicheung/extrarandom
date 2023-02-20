from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README").read_text()

setup(
    name="extrarandom",
    version="1.0.1",
    description="More random utils",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/tovicheung/extrarandom",
    author="tovicheung",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="random",
    packages=find_packages("extrarandom"),
)