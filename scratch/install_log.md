Mon 11 Sep 2023 06:27:53 PM PDT

## The path to a devel environment

### pyenv
From
* [My Goldilocks Python Setup: pyenv, pipx, and pip-tools](https://davidamos.dev/my-goldilocks-python-set-up/)
* https://github.com/pyenv/pyenv?ref=davidamos.dev#installation

`curl https://pyenv.run | bash`

Then add to .bashrc
```
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
And `exec "$SHELL"`

Then dependencies
```
sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

For this project, we need to run on an old Linux Mint running 3.6.9.
`pyenv install 3.6.9`   Which took <2minutes to download and install

```
pyenv shell 3.6.9
cd $project_root
python -m venv venv
pyenv local 3.6.9
source venv/bin/activate
pip install --upgrade pip
pip install pip-tools
```

Now running from VScode

###  Install some packages and retest
```
pip install numpy wave
arecord -D plughw:1,0 -f cd | ./03.py   # Works in scratch/simpleGUI-testing/chatgpt
```

