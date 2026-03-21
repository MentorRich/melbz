#!/bin/sh
# Generate search index from Hugo public dir
SITE_DIR="/data/.openclaw/workspace/sites/tier1/melbz"
PUBLIC_DIR="$SITE_DIR/public"
OUTPUT="$PUBLIC_DIR/index.json"

# Generate a simple search index from HTML titles and paths
python3 -c "
import os, json, re

public = '$PUBLIC_DIR'
index = []
for root, dirs, files in os.walk(public):
    for f in files:
        if f == 'index.html':
            path = os.path.join(root, f)
            rel = os.path.dirname(path).replace(public, '') + '/'
            if rel == '//': rel = '/'
            try:
                with open(path, 'r', errors='replace') as fh:
                    html = fh.read(2000)
                    title_m = re.search(r'<title>(.*?)</title>', html)
                    title = title_m.group(1).split('|')[0].strip() if title_m else ''
                    parts = rel.strip('/').split('/')
                    section = parts[0] if parts[0] else 'home'
                    index.append({'title': title, 'url': rel, 'section': section})
            except: pass

with open('$OUTPUT', 'w') as out:
    json.dump(index, out)
print(f'Search index: {len(index)} pages')
" 2>&1
