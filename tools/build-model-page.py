#!/usr/bin/env python3
"""Build model.html from index.html.

model.html is the same page that opens on the model portfolio, with its own title and
share preview. Run this after every change to index.html and commit both files:

    python3 tools/build-model-page.py
"""
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
s = (root / 'index.html').read_text(encoding='utf-8')


def swap(pattern, repl):
    global s
    s, n = re.subn(pattern, lambda m: repl, s, count=1)
    assert n == 1, pattern


swap(r'<html lang="en">', '<html lang="en" data-default="model">')
swap(r'<title>.*?</title>', '<title>Prim Phunnapa Supakijsilp · Model portfolio</title>')
swap(r'<meta name="description" content="[^"]*">',
     '<meta name="description" content="Model portfolio of Prim Phunnapa Supakijsilp, Bangkok. Compcard, recent shoots with Peucha, OMAKASEN and Sud.performance, and measurements.">')
swap(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="Prim Phunnapa Supakijsilp, model portfolio">')
swap(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="Compcard, recent shoots and measurements. Based in Bangkok.">')
swap(r'<meta property="og:image" content="[^"]*">', '<meta property="og:image" content="images/og-model.jpg">')

(root / 'model.html').write_text(s, encoding='utf-8')
print('wrote model.html')
