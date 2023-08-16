#!/bin/bash

rm -Rf dist
mkdir dist && mkdir dist/python
cp -R lib/python3.9/site-packages/ dist/python/
cd dist

zip -r layer.zip .
rm -Rf python