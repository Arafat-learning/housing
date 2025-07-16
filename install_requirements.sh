#!/bin/bash

# Look for requirements.txt
if [ -f webscraper/requirements.txt ]; then
	echo "Found requirements.txt, installing dependencies..."
	pip install --no-cache-dir -r webscraper/requirements.txt
	echo "Dependencies installed!"
else 
	echo "No requirements.txt, skipping installation of dependencies"
fi

exec bash