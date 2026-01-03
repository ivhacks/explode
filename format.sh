#!/bin/bash

# Clean up imports and fix other issues
python -m ruff check --select I --fix *.py
python -m ruff check --fix *.py

# Format code
python -m ruff format *.py

rm -f ./*.blend[0-9] ./*.blend[0-9][0-9]