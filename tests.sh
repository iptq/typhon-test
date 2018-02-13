#!/bin/bash
PYTHON=python3
PYTHONPATH=$(pwd)/parser
$PYTHON -m pytest . -v