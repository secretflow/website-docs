#!/usr/bin/env bash

pip install -r requirements.txt -r docs/requirements.txt

python -m sphinx -T -E -b mdx -D language=en docs docs/_build/mdx/en-US
