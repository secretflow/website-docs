#!/usr/bin/env bash

pip install -r requirements.txt -r docs/requirements.txt

rm -rf docs/source
SPHINX_APIDOC_OPTIONS=members,autosummary sphinx-apidoc -f -d 2 -t templates -o docs/source secretflow

python -m sphinx -T -E -b mdx -D language=en docs docs/_build/mdx/en-US
python -m sphinx -T -E -b mdx -D language=zh_CN docs docs/_build/mdx/zh-Hans
