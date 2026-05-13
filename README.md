# python-fastapi

Random quotes API on FastAPI 0.115 / Python 3.13 — AppPaaS Pivot sample.

## Run
```
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}
```

## Endpoints
- `GET /` — HTML page with "New quote" button
- `GET /quote`, `GET /quote/{tag}`, `GET /quotes`, `GET /healthz`
