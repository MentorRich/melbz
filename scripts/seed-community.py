#!/usr/bin/env python3
"""
MELBZ Community Seeding Script
Uses editorial personas to simulate initial community activity
"""

import random
from datetime import datetime, timedelta

# MELBZ Editorial Personas
PERSONAS = {
    "lina": {"suburb": "collingwood", "reputation": 89, "voice": "witty, insightful, food-obsessed"},
    "marcus": {"suburb": "carlton", "reputation": 47, "voice": "caffeine-nerd, beer enthusiast"},
    "sofia": {"suburb": "fitzroy", "reputation": 124, "voice": "artistic, culture-focused"},
    "james": {"suburb": "richmond", "reputation": 56, "voice": "sports, pub grub"},
    "emma": {"suburb": "st-kilda", "reputation": 78, "voice": "beach-vibes, nightlife"},
    "oliver": {"suburb": "brunswick", "reputation": 91, "voice": "hipster, indie music"},
    "charlotte": {"suburb": "south-yarra", "reputation": 112, "voice": "fashion, fine dining"},
    "liam": {"suburb": "north-melbourne", "reputation": 34, "voice": "local, family-focused"},
    "ava": {"suburb": "prahran", "reputation": 67, "voice": " brunch-queen, shopping"},
    "jack": {"suburb": "footscray", "reputation": 45, "voice": " multicultural, authentic"},
}

CONFESSIONS = [
    ("I still don't know if I should tip at Australian cafes even though I've lived here 8 years.", "fitzroy", ["😂 23", "💀 5", "🤔 12"]),
    ("Pretended to be a regular at a new cafe. Asked for a cortado. I'd never actually had one.", "carlton", ["😂 34", "👏 8", "😂 15"]),
    ("I judge people who work from home but go to cafes every day. I am those people.", "collingwood", ["🔥 45", "💀 12", "😂 28"]),
    ("Told my date I love jazz. I don't. Three years later, we're married and I own 47 jazz records.", "st-kilda", ["❤️ 67", "😂 89", "🙏 23"]),
    ("I've been going to 'that' indie cafe for 6 months. Found out last week it's a chain.", "carlton", ["💀 34", "😂 45", "👀 18"]),
    ("I faked being a wine expert at a dinner party. I drink Boxed Wine. I'm not sorry.", "south-yarra", ["😂 56", "👏 23", "💀 8"]),
    ("I live in Brunswick and I've never been to CERES. I'm the fraud.", "brunswick", ["😂 78", "🔥 12", "💀 5"]),
    ("The reason I work from home is I can't afford $7 flat whites anymore.", "melbourne", ["🔥 156", "😂 89", "❤️ 34"]),
    ("I told my friends I was 'exploring my creative side' when I started an Instagram. I post photos of my lunch.", "fitzroy", ["😂 45", "👀 23", "😂 12"]),
    ("I've lived in Melbourne 10 years and still can't navigate the tram system properly.", "melbourne", ["🔥 234", "😂 167", "💀 45"]),
]

LOUNGE_TOPICS = [
    {"title": "Best ramen in Melbourne? 👑", "suburb": "melbourne", "replies": 12, "author": "lina"},
    {"title": "Is $7 flat white a rip-off? 🗳️", "suburb": "melbourne", "replies": 34, "author": "marcus"},
    {"title": "Hidden bars in Fitzroy — don't say MoVida", "suburb": "fitzroy", "replies": 23, "author": "sofia"},
    {"title": "Best pub trivia in Richmond?", "suburb": "richmond", "replies": 8, "author": "james"},
    {"title": "Brunch in St Kilda — overrated or perfect?", "suburb": "st-kilda", "replies": 19, "author": "emma"},
    {"title": "Best cheap eats in Brunswick under $20", "suburb": "brunswick", "replies": 15, "author": "oliver"},
    {"title": "Coffee recommendations near South Yarra station", "suburb": "south-yarra", "replies": 7, "author": "charlotte"},
    {"title": "Is North Melbourne just a highway?", "suburb": "north-melbourne", "replies": 12, "author": "liam"},
    {"title": "Chapel Street — still worth it?", "suburb": "prahran", "replies": 21, "author": "ava"},
    {"title": "Footscray market vs Dandenong market?", "suburb": "footscray", "replies": 14, "author": "jack"},
]

VOTES = [
    {"question": "Is $7 too much for a flat white?", "options": ["Yes, robbery", "Nah, fair enough", "Depends on the venue"], "votes": [234, 156, 89], "suburb": "melbourne"},
    {"question": "Best pasta in Melbourne?", "options": ["Carlton", "Fitzroy", "South Yarra", " Richmond"], "votes": [89, 67, 45, 34], "suburb": "melbourne"},
    {"question": "Coffee order?", "options": ["Flat white", "Long black", "Piccolo", "Magic"], "votes": [456, 234, 123, 89], "suburb": "all"},
]

def generate_seed_content():
    """Generate seed content using personas"""
    print("🎲 MELBZ Community Seeding")
    print("=" * 40)
    
    # Generate confessions with persona responses
    print(f"\n📝 {len(CONFESSIONS)} seeded confessions")
    for i, (text, suburb, reactions) in enumerate(random.sample(CONFESSIONS, min(5, len(CONFESSIONS))), 1):
        author = random.choice(list(PERSONAS.keys()))
        print(f"  {i}. [{suburb}] {text[:50]}... — {PERSONAS[author]['suburb']}")
    
    # Generate lounge topics
    print(f"\n💬 {len(LOUNGE_TOPICS)} seeded lounge topics")
    for topic in random.sample(LOUNGE_TOPICS, min(5, len(LOUNGE_TOPICS))):
        author = PERSONAS[topic['author']]
        print(f"  • [{topic['suburb']}] {topic['title']} — {topic['replies']} replies")
    
    # Generate votes
    print(f"\n🗳️ {len(VOTES)} active votes")
    for vote in VOTES:
        print(f"  • [{vote['suburb']}] {vote['question']}")
    
    print("\n" + "=" * 40)
    print("✅ Community seed content generated")
    print("📊 Ready for deployment to melbz.com.au")
    
    # Return content for Hugo integration
    return {
        "confessions": CONFESSIONS[:5],
        "lounge_topics": LOUNGE_TOPICS[:5],
        "votes": VOTES,
        "personas": PERSONAS,
        "generated_at": datetime.now().isoformat()
    }

if __name__ == "__main__":
    seed_data = generate_seed_content()
    print(f"\n📦 Seed data ready for Hugo integration")