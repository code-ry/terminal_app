#!/bin/bash
# Check whether the user has Python installed
if ! [[ -x "$(command -v python)" ]]
then
  echo 'Error: 
    This program runs on Python, but it looks like Python is not installed.
    To install Python, check out https://installpython3.com/' >&2
  exit 1
fi
# Initializes a virtual environment for the user
python3 -m venv .venv
source .venv/bin/activate
# Installs required packages for python
pip install -r requirements.txt
# Runs Program
python3 main.py