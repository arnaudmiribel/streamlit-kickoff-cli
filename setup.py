from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.readlines()

description = (
    "stk is a CLI that helps you kickoff a new Streamlit project"
    " so you can start crafting the app as soon as possible!"
)

long_description = (
    description
    + " It also includes convenient commands like `dev` to open your app in VS"
    " Code + browser automatically and `list` to list all your running"
    " apps... Not forgetting `kill` if you want to turn off an app!"
)

setup(
    name="streamlit-kickoff-cli",
    version="0.1",
    author="Arnaud Miribel",
    author_email="arnaudmiribel@gmail.com",
    url="https://github.com/arnaudmiribel/streamlit-kickoff-cli",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts": ["stk = source.main"]},
    classifiers=("Programming Language :: Python :: 3",),
    keywords="streamlit cli",
    install_requires=requirements,
    zip_safe=False,
)
