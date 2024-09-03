fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── items.py
│   │   │   └── users.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── item.py
│   │   ├── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── item.py
│   │   ├── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── item_service.py
│   │   ├── user_service.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── session.py
│   └── tests/
│       ├── __init__.py
│       ├── test_items.py
│       ├── test_users.py
├── alembic/
│   ├── versions/
│   │   └── 12345_add_users_table.py
├── alembic.ini
├── requirements.txt
├── .env
└── README.md
