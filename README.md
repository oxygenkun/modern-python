# modern-python

Practice of the [
hypermodern python tutorial](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)

# Changes

## Step 1

1. Install **pyenv**

You should follow [the official installation guide](https://github.com/pyenv/pyenv#installation).

Differnet OS needs different script to be added. The tutorial's script exported to the `.bashrc` is not enough.

2. Encounter no sqlite error

[solution](https://stackoverflow.com/a/38842600).

Which would happen if you dose not install some *pyenv* [pre-request libs](https://github.com/pyenv/pyenv/wiki/Common-build-problems).

3. Install **Poetry**

Use `install-poetry.py` to install *poetry*. (`get-poetry.py` is [deprecated](https://python-poetry.org/docs/#installation))

## Step 2

## Step 3

1. Using walk-around function `install_with_constraints` in `noxfile.py`

Add `"--without-hashes",` for avoiding error occurs (Not good enough).

[Some disscussion](https://github.com/cjolowicz/hypermodern-python/issues/174)
