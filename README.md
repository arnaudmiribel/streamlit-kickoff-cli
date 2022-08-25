# streamlit-kickoff-cli 👞

[![PyPI](https://img.shields.io/pypi/v/streamlit-kickoff-cli)](https://pypi.org/project/streamlit-kickoff-cli/)

**A simple CLI to kickoff and manage Streamlit projects**

`stk` is a command-line interface that helps you create, manage and iterate on your Streamlit projects!

---

![CleanShot 2022-08-25 at 15 38 30](https://user-images.githubusercontent.com/7164864/186680001-da90e017-fb13-4305-9138-f07fee420da0.gif)


<p align="center">
    <img src="https://user-images.githubusercontent.com/7164864/186678966-f489514c-b26f-4533-8e94-a43d2ce0bb52.gif" width=1000></img>
</p>

---

## Installation

This is a working setup using Mac OSX & VS Code.

```bash
pip install streamlit-kickoff-cli
```

## Usage

```bash
$ stk --help
```

Commands:
- new   🆕 Create a new Streamlit project
- dev   👩‍💻 Dev time! Opens VS Code and your app in Chrome!
- kick  🚀 New app + dev set up NOW!
- list  🤯 List running Streamlit apps under ports 85**
- kill  🔫 Kill a given Streamlit app running locally!


## Troubleshooting

- Make sure your CLI can access VS Code. See [this link](https://stackoverflow.com/a/40129135/6159698).

- If you get `xcrun: error: invalid active developer path`... error:
Visit https://apple.stackexchange.com/a/254381 or run:
```
xcode-select --install
```
