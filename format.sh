#!/bin/bash

# Clean up imports and fix other issues
python -m ruff check --select I --fix *.py
python -m ruff check --fix *.py

# Format code
python -m ruff format *.py