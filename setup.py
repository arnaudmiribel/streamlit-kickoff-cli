from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.readlines()

long_description = "st is a CLI that helps you kick-off a new Streamlit  \
    project so you can start crafting the app as soon as possible!"

setup(
    name="st-kickoff",
    version="0.1",
    author="Arnaud Miribel",
    author_email="arnaudmiribel@gmail.com",
    url="https://github.com/arnaudmiribel/st",
    description="st is a CLI that helps you kick-off a new Streamlit project \
         so you can start crafting the app as soon as possible!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts": ["st = source.main:go"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ),
    keywords="streamlit cli",
    install_requires=requirements,
    zip_safe=False,
)