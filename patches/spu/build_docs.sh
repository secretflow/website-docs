#!/usr/bin/env bash

pip install -r requirements.txt -r docs/requirements.txt

ls -la /usr/local/lib/python3.8/site-packages/spu

python -m sphinx -T -E -b mdx -D language=en docs docs/_build/mdx/en-US
