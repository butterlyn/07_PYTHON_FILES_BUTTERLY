import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-butterlyn", # Replace with your own username
    version="0.0.2",
    author="Nicholas Butterly",
    author_email="butterlyn888@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown", # specifies .txt or .md README file
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)