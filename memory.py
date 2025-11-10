import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    """Load sent news from memory file."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return set(json.load(f))
    return set()

def save_memory(memory):
    """Save sent news to memory file."""
    with open(MEMORY_FILE, 'w') as f:
        json.dump(list(memory), f)

def add_to_memory(news_items, memory):
    """Add new news items to memory."""
    for item in news_items:
        memory.add(item)
    save_memory(memory)
