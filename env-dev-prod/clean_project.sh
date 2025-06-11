#!/bin/bash

rm -rf .venv
rm -rf .pytest_cache
find . -name '__pycache__' -type d -exec rm -rf {} \;
find . -name '*.egg-info' -type d -exec rm -rf {} \;
