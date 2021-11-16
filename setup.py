import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptocompare-python",
    version="0.0.2",
    author="Alejandro Puig Fuentes",
    author_email="apuig0502@gmail.com",
    description="See currency changes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alejandro193/CryptoCurrency",
    project_urls={
        "Bug Tracker": "https://github.com/Alejandro193/CryptoCurrency.gitissues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.0",
)