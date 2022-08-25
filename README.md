# streamlit-kickoff-cli 👞

[![PyPI](https://img.shields.io/pypi/v/streamlit-kickoff-cli)](https://pypi.org/project/streamlit-kickoff-cli/)
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Farnaudmiribel%2Fstreamlit-kickoff-cli&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=visits&edge_flat=false"/></a>

**A simple CLI to kickoff and manage Streamlit projects**

`stk` is a command-line interface that helps you create, manage and iterate on your Streamlit projects!

---

<p align="center">
    <img src="https://user-images.githubusercontent.com/7164864/186680966-f70851a6-867a-4608-a52c-aa139d0ebf20.gif"></img>
</p>

---

## Installation

This is a working setup using Mac OSX & VS Code.

```bash
pip install streamlit-kickoff-cli
```

## Usage

```
$ stk --help

Usage: stk [OPTIONS] COMMAND [ARGS]...

  Welcome to stk 👞

  This is a simple CLI to help you kick off and maintain Streamlit projects as
  fast as possible!

Options:
  --help  Show this message and exit.

Commands:
  new   🆕 Create a new Streamlit project
  dev   👩‍💻 Dev time! Opens VS Code and your app in Chrome!
  kick  🚀 New app + dev set up NOW!
  list  🤯 List running Streamlit apps under ports 85**
  kill  🔫 Kill a given Streamlit app running locally!
```

## Troubleshooting

- Make sure your CLI can access VS Code. See [this link](https://stackoverflow.com/a/40129135/6159698).

- If you get `xcrun: error: invalid active developer path`... error:
Visit https://apple.stackexchange.com/a/254381 or run:
```
xcode-select --install
```
