# Collections

## Overview

Collections is a simple webapp that allows users to create
and maintain multiple collections of things. The webapp is
to be lightweight and flexible.

Collections are generic and customizable - users can define
their own fields for items within each collection via the
`item_data` JSON field.

## Architecture

Versions:

- Sqlite v. 3.50.4
- Uv v. 3.10
- Django v. 5.2.7
- React v. 19.2.0
- Docker

## Project Structure

```
/
├── config/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── collections_app/     # Main Django app
│   ├── models.py        # Collection and Item models
│   ├── views.py         # API views
│   ├── admin.py
│   └── migrations/
├── manage.py            # Django management script
├── database.db          # SQLite database
└── pyproject.toml       # UV dependencies
```

## Data Models

### Collection
- `id`: Auto-generated primary key
- `name`: CharField - name of the collection

### Item
- `id`: Auto-generated primary key
- `name`: CharField - name of the item
- `item_data`: JSONField - flexible JSON storage for custom fields
- `collection`: ForeignKey to Collection (CASCADE delete)

The `item_data` field stores custom collection fields as JSON,
allowing each collection to have its own unique schema.
