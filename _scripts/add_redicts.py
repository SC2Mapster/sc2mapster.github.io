#!/usr/bin/env python

from os import path
from glob import glob
import subprocess


def run(x) -> str:
    print(x)
    p: subprocess.CompletedProcess = subprocess.run(x, capture_output=True, shell=True)
    assert p.returncode == 0
    return p.stdout.decode('utf-8').strip()


for srcName in glob('%s/**/*.md' % '_editor_tutorials'):
    link = path.splitext(path.relpath(srcName, '_editor_tutorials'))[0]
    out = []
    out.append('---')
    try:
        out.append(run('cat %s | rg "title:"' % srcName))
    except AssertionError:
        out.append('title: %s' % path.basename(link)[4:].replace('_', ' '))
    out.append('redirect_to: https://s2editor-guides.readthedocs.io/New_Tutorials/%s' % link)
    out.append('---')
    with open(srcName, 'w') as f:
        f.write('\n'.join(out) + '\n')
