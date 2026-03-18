#!/usr/bin/env python3
"""
MELBZ Pexels Image Fetcher
Uses Pexels API to fetch relevant images for articles based on topic.
Uses urllib (built-in) instead of requests.
"""

import os
import re
import random
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# Pexels API Configuration
PEXELS_API_KEY = "pdGT8KCm8egeDa5CKSz9vRRIFi8ykLsZtdDWHXedjd35j3J3jrw9uZWg"
PEXELS_SEARCH_URL = "https://api.pexels.com/v1/search"

# Search queries by article type
SEARCH_QUERIES = {
    'cafe': ['melbourne cafe coffee', 'café interior melbourne', 'coffee shop melbourne'],
    'coffee': ['coffee latte melbourne', 'barista melbourne', 'coffee shop'],
    'brunch': ['brunch melbourne', 'breakfast avo toast', 'breakfast melbourne'],
    'restaurant': ['restaurant melbourne', 'fine dining melbourne', 'restaurant interior'],
    'dining': ['dinner melbourne', 'restaurant food melbourne'],
    'asian': ['asian food melbourne', 'noodle soup melbourne', 'dim sum melbourne'],
    'bar': ['cocktail bar melbourne', 'wine bar melbourne', 'bar interior'],
    'pub': ['pub melbourne', 'beer garden melbourne', 'australian pub'],
    'nightlife': ['melbourne nightlife', 'night club melbourne', 'party melbourne'],
    'nightlife-guide': ['melbourne night scene', 'cocktails melbourne'],
    'food': ['gourmet food melbourne', 'plated food photography'],
    'cheap': ['street food melbourne', 'cheap eats melbourne', 'food market'],
    'things-to-do': ['melbourne city', 'things to do melbourne', 'tourist melbourne'],
    'things-to-do-this-weekend': ['weekend melbourne', 'events melbourne'],
    'activities': ['activity melbourne', 'adventure melbourne'],
    'date-night': ['romantic dinner melbourne', 'couple date melbourne'],
    'new-openings': ['new restaurant melbourne', 'opening melbourne'],
    'neighbourhood-guide': ['melbourne suburb street', 'neighbourhood melbourne'],
    'suburb-guide': ['melbourne suburb', 'australian suburb'],
    'art': ['art gallery melbourne', 'street art melbourne', 'art exhibition'],
    'galleries': ['art gallery', 'contemporary art'],
    'transport': ['tram melbourne', 'public transport melbourne'],
    'cycling': ['bike melbourne', 'cycling melbourne'],
    'rent': ['apartment melbourne', 'real estate melbourne'],
    'cost-of-living': ['melbourne city living', 'urban lifestyle'],
    'student': ['university melbourne', 'student life melbourne'],
    'happy-hour': ['happy hour melbourne', 'drinks deals melbourne'],
    'live-music': ['live music melbourne', 'concert melbourne'],
    'pizza': ['pizza melbourne', 'italian food melbourne'],
    'dog-friendly': ['dog friendly melbourne', 'outdoor dining'],
    'culture': ['melbourne culture', 'arts melbourne'],
    'honest-guide': ['melbourne street', 'city life melbourne'],
    'default': ['melbourne cityscape', 'australia urban', 'victoria melbourne'],
}

# Cache for image URLs to avoid repeated API calls
image_cache = {}

def search_pexels(query, per_page=5):
    """Search Pexels for images matching the query"""
    if query in image_cache:
        return image_cache[query]
    
    try:
        headers = {"Authorization": PEXELS_API_KEY}
        url = f"{PEXELS_SEARCH_URL}?query={query}&per_page={per_page}&size=large"
        req = Request(url, headers=headers)
        
        with urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            photos = data.get('photos', [])
            if photos:
                urls = []
                for photo in photos:
                    src = photo.get('src', {})
                    url = src.get('large') or src.get('medium') or src.get('original')
                    if url:
                        urls.append(url)
                image_cache[query] = urls
                return urls
    except (URLError, HTTPError, json.JSONDecodeError) as e:
        print(f"  Pexels error for '{query}': {type(e).__name__}")
    
    return None

def get_image_for_article(article_name):
    """Get a relevant image URL for an article based on its filename"""
    name = article_name.lower().replace('.md', '').replace('-', ' ')
    
    # Try exact and partial matches
    for key, queries in SEARCH_QUERIES.items():
        if key in name or name in key:
            for query in queries:
                urls = search_pexels(query)
                if urls:
                    return random.choice(urls)
    
    # Fall back to default
    for query in SEARCH_QUERIES['default']:
        urls = search_pexels(query)
        if urls:
            return random.choice(urls)
    
    return None

def update_article_image(filepath, new_url):
    """Update the cover_image in article frontmatter"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match cover_image with quotes
    pattern = r'cover_image:\s*"https?://[^"]+"'
    
    if re.search(pattern, content):
        new_content = re.sub(pattern, f'cover_image: "{new_url}"', content)
    else:
        # Try pattern without quotes
        pattern2 = r'cover_image:\s*https?://[^\s]+'
        if re.search(pattern2, content):
            new_content = re.sub(pattern2, f'cover_image: "{new_url}"', content)
        else:
            return False
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def process_articles(content_dir, limit=None):
    """Process articles and update their images"""
    articles = []
    for root, dirs, files in os.walk(content_dir):
        for filename in files:
            if not filename.endswith('.md') or filename.startswith('_'):
                continue
            filepath = os.path.join(root, filename)
            articles.append((filepath, filename))
    
    if limit:
        articles = articles[:limit]
    
    updated = 0
    failed = 0
    
    for filepath, filename in articles:
        new_url = get_image_for_article(filename)
        if new_url:
            if update_article_image(filepath, new_url):
                print(f'✓ {filename}')
                updated += 1
            else:
                print(f'✗ {filename} (update failed)')
                failed += 1
        else:
            print(f'✗ {filename} (no image)')
            failed += 1
    
    return updated, failed

if __name__ == '__main__':
    import sys
    
    content_dir = sys.argv[1] if len(sys.argv) > 1 else './content'
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
    
    print('🖼 MELBZ Pexels Image Fetcher')
    print('=' * 40)
    print(f'Content dir: {content_dir}')
    print(f'Limit: {limit or "All"}')
    print('=' * 40)
    
    updated, failed = process_articles(content_dir, limit)
    
    print('=' * 40)
    print(f'Updated: {updated}')
    print(f'Failed: {failed}')
    print(f'Cached queries: {len(image_cache)}')