#!/usr/bin/env python3
"""
MELBZ Article Image Updater
Updates article cover images based on article type (filename) using Unsplash free images.
"""

import os
import re
import random
from pathlib import Path

# Image mapping: article type → list of relevant Unsplash image URLs
IMAGE_MAP = {
    # Cafe & Coffee articles
    'cafe': [
        'https://images.unsplash.com/photo-1521017432531-fbd92d768814?w=800&q=80',
        'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?w=800&q=80',
        'https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=800&q=80',
        'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800&q=80',
    ],
    'coffee': [
        'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?w=800&q=80',
        'https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=800&q=80',
        'https://images.unsplash.com/photo-1521017432531-fbd92d768814?w=800&q=80',
    ],
    'brunch': [
        'https://images.unsplash.com/photo-1533089862017-5614a9571467?w=800&q=80',
        'https://images.unsplash.com/photo-1466978913421-dad2ebd01d17?w=800&q=80',
        'https://images.unsplash.com/photo-1484723091739-30a097e8f929?w=800&q=80',
    ],
    # Restaurant & Dining
    'restaurant': [
        'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80',
        'https://images.unsplash.com/photo-1552566626-52f8b828add9?w=800&q=80',
        'https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&q=80',
    ],
    'dining': [
        'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80',
        'https://images.unsplash.com/photo-1559339352-11d035aa65de?w=800&q=80',
    ],
    'asian': [
        'https://images.unsplash.com/photo-1563245372-f21724e3856d?w=800&q=80',
        'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=800&q=80',
        'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=800&q=80',
    ],
    # Bars & Nightlife
    'bar': [
        'https://images.unsplash.com/photo-1470337458703-46ad1756a187?w=800&q=80',
        'https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800&q=80',
        'https://images.unsplash.com/photo-1572116469696-31de0f17cc34?w=800&q=80',
    ],
    'pub': [
        'https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=800&q=80',
        'https://images.unsplash.com/photo-1546173159-315724a31696?w=800&q=80',
    ],
    'nightlife': [
        'https://images.unsplash.com/photo-1470337458703-46ad1756a187?w=800&q=80',
        'https://images.unsplash.com/photo-1496417263034-38ec4f0d665a?w=800&q=80',
        'https://images.unsplash.com/photo-1514525253440-b393452e8d03?w=800&q=80',
    ],
    'nightlife-guide': [
        'https://images.unsplash.com/photo-1514525253440-b393452e8d03?w=800&q=80',
        'https://images.unsplash.com/photo-1496417263034-38ec4f0d665a?w=800&q=80',
    ],
    # Food & Eating
    'food': [
        'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800&q=80',
        'https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=800&q=80',
    ],
    'cheap': [
        'https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800&q=80',
        'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&q=80',
        'https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=800&q=80',
    ],
    # Activities & Things to Do
    'things-to-do': [
        'https://images.unsplash.com/photo-1503767849114-0d87a13c14b0?w=800&q=80',
        'https://images.unsplash.com/photo-1468665957224-2756d4dc4d2e?w=800&q=80',
    ],
    'things-to-do-this-weekend': [
        'https://images.unsplash.com/photo-1468665957224-2756d4dc4d2e?w=800&q=80',
        'https://images.unsplash.com/photo-1533174072545-e8d4aa97edf9?w=800&q=80',
    ],
    'activities': [
        'https://images.unsplash.com/photo-1503767849114-0d87a13c14b0?w=800&q=80',
        'https://images.unsplash.com/photo-1532712938310-34cb395fd7c2?w=800&q=80',
    ],
    # Date Night & Events
    'date-night': [
        'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&q=80',
        'https://images.unsplash.com/photo-1514525253440-b393452e8d03?w=800&q=80',
        'https://images.unsplash.com/photo-1545167622-3a6ac756afa4?w=800&q=80',
    ],
    'new-openings': [
        'https://images.unsplash.com/photo-1552566626-52f8b828add9?w=800&q=80',
        'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&q=80',
    ],
    # Suburb/Neighborhood guides
    'neighbourhood-guide': [
        'https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=800&q=80',
        'https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=800&q=80',
    ],
    'suburb-guide': [
        'https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=800&q=80',
    ],
    # Arts & Culture
    'art': [
        'https://images.unsplash.com/photo-1531243269054-5ebf6f34081e?w=800&q=80',
        'https://images.unsplash.com/photo-1561055657-b9e0bf0fa360?w=800&q=80',
    ],
    'galleries': [
        'https://images.unsplash.com/photo-1531243269054-5ebf6f34081e?w=800&q=80',
    ],
    # Transport & Living
    'transport': [
        'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800&q=80',
        'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&q=80',
    ],
    'cycling': [
        'https://images.unsplash.com/photo-1541625602330-2277a4c46182?w=800&q=80',
    ],
    'rent': [
        'https://images.unsplash.com/photo-1460317442991-0ec209397118?w=800&q=80',
    ],
    'cost-of-living': [
        'https://images.unsplash.com/photo-1460317442991-0ec209397118?w=800&q=80',
    ],
    # Default fallback
    'default': [
        'https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=800&q=80',
        'https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=800&q=80',
    ],
}

def get_article_type(filename):
    """Extract article type from filename"""
    # Remove .md extension and convert to lowercase
    name = filename.lower().replace('.md', '')
    return name

def find_matching_images(article_type, suburb=''):
    """Find appropriate images for an article based on its type"""
    # Check for exact matches first
    if article_type in IMAGE_MAP:
        images = IMAGE_MAP[article_type]
        return random.choice(images)
    
    # Check for partial matches
    for key, images in IMAGE_MAP.items():
        if key in article_type or article_type in key:
            return random.choice(images)
    
    # Check suburb-specific images (future enhancement)
    # For now, return a random default image
    return random.choice(IMAGE_MAP['default'])

def update_article_image(filepath, new_image_url):
    """Update the cover_image in article frontmatter"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if cover_image already exists
    if 'cover_image:' in content:
        # Replace existing cover_image
        pattern = r'cover_image:\s*https?://[^\s]+'
        new_content = re.sub(pattern, f'cover_image: {new_image_url}', content)
    elif 'cover_image =' in content:
        # Handle TOML format
        pattern = r'cover_image\s*=\s*"https?://[^"]+"'
        new_content = re.sub(pattern, f'cover_image = "{new_image_url}"', content)
    else:
        # Add cover_image after title
        if 'title:' in content or 'title =' in content:
            # Insert after the first line (title)
            lines = content.split('\n', 1)
            new_content = lines[0] + f'\ncover_image: {new_image_url}\n' + lines[1]
        else:
            # Just append at the beginning
            new_content = f'cover_image: {new_image_url}\n{content}'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def process_articles(content_dir):
    """Process all markdown articles and update their images"""
    updated_count = 0
    skipped_count = 0
    
    for root, dirs, files in os.walk(content_dir):
        for filename in files:
            if not filename.endswith('.md'):
                continue
            
            filepath = os.path.join(root, filename)
            
            # Get relative path from content directory
            rel_path = os.path.relpath(filepath, content_dir)
            article_type = get_article_type(filename)
            
            # Skip certain files
            if filename.startswith('_index') or filename == 'index.md':
                continue
            
            # Get suburb from path (second level directory)
            parts = rel_path.split(os.sep)
            suburb = parts[0] if len(parts) > 1 else ''
            
            # Find appropriate image
            new_image = find_matching_images(article_type, suburb)
            
            # Update the article
            try:
                update_article_image(filepath, new_image)
                print(f'✓ Updated: {rel_path} → {article_type}')
                updated_count += 1
            except Exception as e:
                print(f'✗ Error updating {rel_path}: {e}')
                skipped_count += 1
    
    return updated_count, skipped_count

if __name__ == '__main__':
    import sys
    
    content_dir = sys.argv[1] if len(sys.argv) > 1 else './content'
    
    print('🖼 MELBZ Article Image Updater')
    print('=' * 40)
    
    updated, skipped = process_articles(content_dir)
    
    print('=' * 40)
    print(f'Updated: {updated} articles')
    print(f'Skipped: {skipped} articles')
    print('Done!')