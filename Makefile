PYENV_NAME=nistai
PYTHON_VERSION=3.11.0
POETRY=poetry

# Environment selection: test, dev, prod
ENV ?= dev
ifeq ($(ENV),prod)
	DEPLOYMENT_TYPE=prod
else
	DEPLOYMENT_TYPE=debug
endif

.PHONY: pyenv-setup
pyenv-setup:
	pyenv install -s $(PYTHON_VERSION)
	pyenv virtualenv -f $(PYTHON_VERSION) $(PYENV_NAME)
	pyenv local $(PYENV_NAME)
	$(POETRY) env use $(PYENV_NAME)
	$(POETRY) install

.PHONY: start
start:
	pyenv exec poetry run uvicorn nistaiapp.asgi:application --reload --host 0.0.0.0 --port 8000

.PHONY: stop
stop:
	pkill -f "uvicorn nistaiapp.asgi:application" || true

.PHONY: docker-up
docker-up:
	DEPLOYMENT_TYPE=prod docker compose up -d --build

.PHONY: docker-down
docker-down:
	docker compose down

.PHONY: create-superuser
create-superuser:
	$(POETRY) run bash create-superuser.sh

.PHONY: reset-db
reset-db:
ifeq ($(ENV),prod)
	@echo "Resetting PostgreSQL database (prod) via Docker Compose..."
	docker compose exec db psql -U $$POSTGRES_USER -d $$POSTGRES_DB -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
	DEPLOYMENT_TYPE=prod $(POETRY) run python manage.py migrate
else
	@echo "Resetting SQLite database (test/dev)..."
	rm -f db.sqlite3
	DEPLOYMENT_TYPE=$(DEPLOYMENT_TYPE) $(POETRY) run python manage.py migrate
endif

.PHONY: load-sample-data
load-sample-data:
	poetry run python manage.py load_sample_data

.PHONY: collectstatic
collectstatic:
	poetry run python manage.py collectstatic --noinput
