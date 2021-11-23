# 🎈 `st` — a CLI to kick-off your Streamlit project

`st` is a CLI that helps you start a new Streamlit project. Here's what `st` does:
- Create a script `streamlit_app.py` file with a basic Streamlit template
- Open that script in VS Code
- Run the Streamlit app
- Open the app in your browser

So you're ready to start crafting the app!

✨ It's as simple as:

```bash
$ st
```

https://user-images.githubusercontent.com/7164864/142880682-e2ac5e67-400e-4eec-bef8-22db7408c9f4.mov


## 🚀 Usage

### Prerequisites

This is a working setup using OSX & VS Code.

### Install

**Using pip:**

Run:
```
$ pip install st-kickoff
```


### Documentation

```
$ st --help

Usage: st [OPTIONS]

Options:
  -p, --path TEXT                 Path where you want to create your Streamlit
                                  project. (Default: ".")

  --open_project_in_vs_code TEXT  Open VS code with the newly created file. (Default: True)
  --run_app TEXT                  Run Streamlit script (Default: True)
  --open_app_in_browser TEXT      Open Streamlit app in browser (Default: True)
  --help                          Show this message and exit.
```

### Get started!

Make a new directory, `cd` in and run:

```
$ st 
```

### Troubleshooting

- Make sure your CLI can access VS Code. See [this link](https://stackoverflow.com/a/40129135/6159698).

- If you get `xcrun: error: invalid active developer path`... error:  
Visit https://apple.stackexchange.com/a/254381 or run:
```
xcode-select --install
```
