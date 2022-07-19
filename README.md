# openapi-to-typescript-example

Example project to show TS code generation from an OpenAPI spec

## Installation and usage

### Backend

```shell
cd backend
python -m virtualenv .venv && source .venv/bin/activate  # recommended
pip install

uvicorn backend:app --reload
```

### Frontend

```shell
cd frontend
yarn install
yarn dev
```

#### Generate Typescript Client 

```shell
# 1. Run backend

# 2. Execute:
yarn make-api
```
