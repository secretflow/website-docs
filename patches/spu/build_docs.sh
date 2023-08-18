#!/usr/bin/env bash

pip install -r requirements.txt -r docs/requirements.txt

pushd docs # this prevents Python from importing unbuilt SPU

python -m sphinx -T -E -b mdx -D language=en . ./_build/mdx/en-US

popd
