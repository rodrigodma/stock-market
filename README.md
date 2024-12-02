# Stock Market API
## Goal
Your assignment is to implement a Stocks REST API using Python and a popular web framework of your choice. It could be but not limited to FastAPI/ Flask/ Django.
## Proposed Solution
**Project Structure**
```
├── src
│   ├── infra
│   │   ├── repository.py
│   │   ├── config.py
│   │   └── db.py
│   ├── repositories
│   │   └── stock_market.py
│   ├── models
│   │   └── stock_market.py
│   ├── schemas
│   │   └── stock_market.py
│   ├── services
│   │   └── stock_market.py
│   └── app.py
└── requirements.txt
```

**requirements.txt:**

```
fastapi
uvicorn
pydantic
sqlalchemy
pytest
pytest-cov
```

**Configuring:**

1. **Virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

**Running:**
1. **Server:**
   ```bash
   uvicorn backend.app:app --reload
   ```

**Observations**
- this is the first version of the project, contains:
-- Stock Market REST API, end-to-end
- next steps:
-- unit, integration and e2e tests
-- connection with postgres db
-- unit test
-- docker environment
-- logging and cache mechanism
-- input data using scrapping approach