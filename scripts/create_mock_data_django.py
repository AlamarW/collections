#!/usr/bin/env python
"""
Script to create mock data for collections app using Django ORM directly.
Run with: uv run python manage.py shell < scripts/create_mock_data_django.py
Or: uv run python scripts/create_mock_data_django.py (after Django setup)
"""

import os
import sys

import django

# Setup Django environment
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth.models import User

from collections_app.models import Collection, Item

# Mock data definitions
COLLECTIONS = [
    {
        "name": "Pokemon Card Collection",
        "description": "My collection of rare and valuable Pokemon trading cards",
        "collection_schema": {
            "name": "",
            "edition": "",
            "condition": "",
            "date_obtained": "",
            "price": "",
        },
        "items": [
            {
                "name": "Charizard",
                "edition": "Base Set 1st Edition",
                "condition": "Near Mint",
                "date_obtained": "2023-05-12",
                "price": "$2,500",
            },
            {
                "name": "Pikachu",
                "edition": "Shadowless Base Set",
                "condition": "Mint",
                "date_obtained": "2023-06-20",
                "price": "$450",
            },
            {
                "name": "Blastoise",
                "edition": "Base Set Unlimited",
                "condition": "Lightly Played",
                "date_obtained": "2022-11-03",
                "price": "$85",
            },
            {
                "name": "Mewtwo",
                "edition": "Base Set 1st Edition",
                "condition": "Near Mint",
                "date_obtained": "2024-01-15",
                "price": "$180",
            },
            {
                "name": "Gyarados",
                "edition": "Team Rocket 1st Edition",
                "condition": "Mint",
                "date_obtained": "2023-08-07",
                "price": "$95",
            },
            {
                "name": "Alakazam",
                "edition": "Base Set Shadowless",
                "condition": "Excellent",
                "date_obtained": "2023-03-22",
                "price": "$120",
            },
            {
                "name": "Venusaur",
                "edition": "Base Set 1st Edition",
                "condition": "Near Mint",
                "date_obtained": "2024-02-10",
                "price": "$650",
            },
            {
                "name": "Dragonite",
                "edition": "Fossil 1st Edition",
                "condition": "Excellent",
                "date_obtained": "2023-09-18",
                "price": "$220",
            },
            {
                "name": "Mew",
                "edition": "Wizards Black Star Promo",
                "condition": "Mint",
                "date_obtained": "2022-12-05",
                "price": "$75",
            },
            {
                "name": "Eevee",
                "edition": "Jungle 1st Edition",
                "condition": "Near Mint",
                "date_obtained": "2023-07-14",
                "price": "$45",
            },
        ],
    },
    {
        "name": "Book Collection",
        "description": "Classic and contemporary literature collection",
        "collection_schema": {
            "title": "",
            "author": "",
            "isbn": "",
            "publication_year": "",
            "notes": "",
        },
        "items": [
            {
                "title": "1984",
                "author": "George Orwell",
                "isbn": "978-0451524935",
                "publication_year": "1949",
                "notes": "First edition hardcover, excellent condition",
            },
            {
                "title": "Dune",
                "author": "Frank Herbert",
                "isbn": "978-0441172719",
                "publication_year": "1965",
                "notes": "Signed copy from book tour",
            },
            {
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "isbn": "978-0743273565",
                "publication_year": "1925",
                "notes": "Vintage paperback",
            },
            {
                "title": "To Kill a Mockingbird",
                "author": "Harper Lee",
                "isbn": "978-0061120084",
                "publication_year": "1960",
                "notes": "Anniversary edition",
            },
            {
                "title": "The Catcher in the Rye",
                "author": "J.D. Salinger",
                "isbn": "978-0316769174",
                "publication_year": "1951",
                "notes": "Original dust jacket",
            },
            {
                "title": "Pride and Prejudice",
                "author": "Jane Austen",
                "isbn": "978-0141439518",
                "publication_year": "1813",
                "notes": "Penguin Classics edition",
            },
            {
                "title": "The Hobbit",
                "author": "J.R.R. Tolkien",
                "isbn": "978-0547928227",
                "publication_year": "1937",
                "notes": "Illustrated edition",
            },
            {
                "title": "Brave New World",
                "author": "Aldous Huxley",
                "isbn": "978-0060850524",
                "publication_year": "1932",
                "notes": "Harper Perennial Modern Classics",
            },
            {
                "title": "The Lord of the Rings",
                "author": "J.R.R. Tolkien",
                "isbn": "978-0544003415",
                "publication_year": "1954",
                "notes": "Complete trilogy boxed set",
            },
            {
                "title": "Fahrenheit 451",
                "author": "Ray Bradbury",
                "isbn": "978-1451673319",
                "publication_year": "1953",
                "notes": "60th anniversary edition",
            },
        ],
    },
    {
        "name": "Vinyl Record Collection",
        "description": "Vintage and rare vinyl records from various genres",
        "collection_schema": {
            "album_name": "",
            "artist": "",
            "release_year": "",
            "label": "",
            "condition": "",
        },
        "items": [
            {
                "album_name": "The Dark Side of the Moon",
                "artist": "Pink Floyd",
                "release_year": "1973",
                "label": "Harvest Records",
                "condition": "Near Mint",
            },
            {
                "album_name": "Abbey Road",
                "artist": "The Beatles",
                "release_year": "1969",
                "label": "Apple Records",
                "condition": "Excellent",
            },
            {
                "album_name": "Led Zeppelin IV",
                "artist": "Led Zeppelin",
                "release_year": "1971",
                "label": "Atlantic Records",
                "condition": "Very Good Plus",
            },
            {
                "album_name": "Rumours",
                "artist": "Fleetwood Mac",
                "release_year": "1977",
                "label": "Warner Bros",
                "condition": "Near Mint",
            },
            {
                "album_name": "The Velvet Underground & Nico",
                "artist": "The Velvet Underground",
                "release_year": "1967",
                "label": "Verve Records",
                "condition": "Very Good",
            },
            {
                "album_name": "Kind of Blue",
                "artist": "Miles Davis",
                "release_year": "1959",
                "label": "Columbia Records",
                "condition": "Excellent",
            },
            {
                "album_name": "Thriller",
                "artist": "Michael Jackson",
                "release_year": "1982",
                "label": "Epic Records",
                "condition": "Near Mint",
            },
            {
                "album_name": "The Wall",
                "artist": "Pink Floyd",
                "release_year": "1979",
                "label": "Harvest Records",
                "condition": "Very Good Plus",
            },
            {
                "album_name": "Sgt. Pepper's Lonely Hearts Club Band",
                "artist": "The Beatles",
                "release_year": "1967",
                "label": "Parlophone",
                "condition": "Excellent",
            },
            {
                "album_name": "Nevermind",
                "artist": "Nirvana",
                "release_year": "1991",
                "label": "DGC Records",
                "condition": "Near Mint",
            },
        ],
    },
]


def main():
    print("Starting mock data creation using Django ORM...")
    print("-" * 50)

    # Get or create testuser
    try:
        user = User.objects.get(username="testuser")
        print(f"✓ Found user: testuser")
    except User.DoesNotExist:
        print("✗ User 'testuser' not found. Please create it first.")
        return

    print()

    # Create collections and items
    total_items = 0
    for collection_data in COLLECTIONS:
        # Create collection
        collection = Collection.objects.create(
            name=collection_data["name"],
            description=collection_data.get("description", ""),
            collection_schema=collection_data["collection_schema"],
            owner=user,
        )
        print(f"✓ Created collection: {collection.name} (ID: {collection.id})")

        # Create items for this collection
        items_created = 0
        for item_data in collection_data["items"]:
            # Extract the name field - different schemas use different key names
            item_name = (
                item_data.get("name")
                or item_data.get("title")
                or item_data.get("album_name")
                or "Unnamed Item"
            )

            item = Item.objects.create(
                name=item_name, item_data=item_data, item_collection=collection
            )
            items_created += 1

        print(f"  ✓ Created {items_created} items")
        total_items += items_created
        print()

    print("-" * 50)
    print(f"Mock data creation complete!")
    print(f"Created {len(COLLECTIONS)} collections with {total_items} total items")


if __name__ == "__main__":
    main()
