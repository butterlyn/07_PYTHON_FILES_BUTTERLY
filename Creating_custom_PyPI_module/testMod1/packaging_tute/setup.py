## DO NOT CHANGE
import setuptools
from markdown import Markdown
from io import StringIO

def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()

Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False

def unmark(text):
    return __md.convert(text)

with open("README.md", "r") as fh:
    long_description = fh.read()
    long_description = unmark(long_description)
    print(long_description)


## CUSTOMISE WITH PACKAGE DETAILS. `#` entries require updating
setuptools.setup(
    name="example-pkg-butterlyn",
    version="0.0.2", # update to latest release version
    author="Nicholas Butterly",
    author_email="butterlyn888@gmail.com",
    description="A small example package", # update with one-sentence package description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/butterlyn/PACKAGE_NAME_IN_GIT", # specify url to package in github
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)