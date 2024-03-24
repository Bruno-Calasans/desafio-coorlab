#!/bin/bash

echo "Executing back-end..."
cd api
pipx install poethepoet
poetry install
poe dev &

echo "Executing front-end..."
cd ../client
npm install
npm run dev