#!/bin/bash
echo "Setting up python environment"
pip3 install virtualenv > /dev/null

if [ -d .env ]; then
	rm -fr .env
fi

virtualenv .env
source .env/bin/activate

echo "Installing python packages"
pip install -r requirements.txt > /dev/null

echo "Setting up nodeenv..."
pip install nodeenv > /dev/null
nodeenv -p

echo "Installing node modules"
pushd kileed/ui > /dev/null
npm install
popd > /dev/null
