#!/bin/bash

# terminate on error
set -e

# change directory to where this script is located
OLDDIR=$(pwd)
DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $DIR

# change directory to where we were on exit
finish () {
    cd $OLDDIR
}
trap 'finish' exit

VERSION="3.4"
assert_python_version() {
    if ! which python3.4 >/dev/null 2>&1; then
        echo "Please install Python3.4"
        exit 1
    fi
}

# install venv if not present, and set up the venv
install_venv() {
    if ! which virtualenv-${VERSION} >/dev/null 2>&1; then
        echo "Installing virtualenv"
        PIPVERSION={VERSION:0:1}
        sudo pip${PIPVERSION} install virtualenv virtualenvwrapper
    fi

    VENV_DIR="$(pwd)/.env"

    if [ ! -d "$VENV_DIR" ]; then
        echo "Creating virtualenv in $VENV_DIR"
        mkdir -p $VENV_DIR
    fi

    virtualenv-${VERSION} $VENV_DIR

    echo "Activating virtualenv"
    source $VENV_DIR/bin/activate
}

# gets sudo up front, exits if not
capture_sudo() {
    if ! sudo echo; then
        echo "You must sudo to continue"
        exit 1
    fi
}

# install the pip packages
install_pippackages() {
    pip${VERSION} install -r requirements.txt
}

capture_sudo
assert_python_version
install_venv
install_pippackages