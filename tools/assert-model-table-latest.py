#!/usr/bin/env python3
from __future__ import annotations
import os, sys
from markdown_it import MarkdownIt
md = MarkdownIt()

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(ROOT, 'README.md'), 'r') as f:
  readme = md.parse(f.read())
sys.path.insert(0, os.path.join(ROOT, 'openllm-python', 'src'))
import openllm

# NOTE: Currently, we only have one table in README, which is the Model readme.
table = [r for r in readme if r.type == 'html_block' and r.content.startswith('<td><a')]

prev = os.environ.pop('OPENLLMDEVDEBUG', None)
available = len(openllm.CONFIG_MAPPING.keys())
if prev: os.environ['OPENLLMDEVDEBUG'] = prev

on_table = len(table)  # NOTE: minus the header

if available - on_table != 0:
  print('README.md is out of date! Make sure to run ./tools/update-readme.py')
  raise SystemExit(1)
raise SystemExit(0)
