# 👨‍🏫 `st`: a friendly instructor CLI

`st` is a CLI that helps you starting a new Streamlit project from the commandl ine

## ✨ How it works

Simple as:

```bash
$ st .
```

#[![np demo](./demo_quick.gif)]()


## 🚀 Usage

### Prerequisites

This is a working setup for anyone using Microsoft VS Code.
Has been tested solely on Mac OSX.

#### Manually

1. Install requirements:

```
pip install -r requirements.txt
```

2. Make sure to enable your CLI to access VS Code. See [this link](https://stackoverflow.com/a/40129135/6159698).

3. Add the alias to your `~/.bash_profile`:
```
# Alias for st
alias st='python ~/your/path/to/st/st.py -p'
```

4. Source it:
```
source ~/.bash_profile
```

### Getting started

Run:

```
$ st {directory}
```

### Documentation


### Troubleshooting

- If you get `xcrun: error: invalid active developer path`... error:  
Visit https://apple.stackexchange.com/a/254381 or run:
```
xcode-select --install
```
