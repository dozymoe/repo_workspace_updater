#!/bin/bash

PYTHON_VERSION=3.4

# system package requirements:
#   - dev-lang/python (appropriate version)
#   - dev-python/pip
#   - dev-python/virtualenv


fatal() {
  message="$1";

  echo "ERROR: $message"
  exit 1
}


# setup python modules
if [[ ! -d .virtualenv ]]
then
    virtualenv --python=python${PYTHON_VERSION} .virtualenv || fatal 'Failed to create virtualenv'
fi

if [[ ! -h python_modules ]]
then
    ln -s .virtualenv/lib/python${PYTHON_VERSION}/site-packages python_modules || fatal 'Failed to create symlink "python_modules"'
fi

[[ ! -r .virtualenv/bin/activate ]] && fatal 'Cannot activate virtualenv'
if [[ -r .virtualenv/bin/activate ]]
then
    . .virtualenv/bin/activate
fi

pip install --upgrade pip || fatal 'Cannot upgrade pip'
pip install -r requirements.txt || fatal  'Cannot install python modules'
