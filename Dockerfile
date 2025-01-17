FROM python:3.11-buster as builder

RUN pip install poetry==1.8.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache


WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN touch README.md

RUN poetry install --no-root && rm -rf $POETRY_CACHE_DIR


FROM python:3.11-slim-buster as runtime


ENV VIRTUAL_ENV=/app/.venv \
PATH="/app/.venv/bin:$PATH"

WORKDIR /app

# COPY --from=builder /app/.venv /app/.venv
COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY . /app



CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]