# NIST AI RMF Django Application

This project implements the NIST AI Risk Management Framework (AI RMF) as a Django web application. It is designed for organizations to manage, assess, and document AI risks in alignment with the NIST AI RMF core functions: Govern, Map, Measure, and Manage.

## Features
- Modular Django apps for each NIST AI RMF core function
- REST API for all models (using Django REST Framework)
- Admin interface for managing policies, risks, metrics, incidents, and more
- Multiple deployment modes: test/dev (SQLite) and prod (PostgreSQL)
- Docker and Docker Compose support
- Easy environment management with pyenv, poetry, and Makefile

## Quick Start

### 1. Clone the repository
```bash
git clone <repo-url>
cd nistrmf
```

### 2. Setup Python environment and dependencies
```bash
make pyenv-setup
```

### 3. Start the application
- For development (SQLite):
  ```bash
  make start ENV=dev
  ```
- For production (PostgreSQL, via Docker Compose):
  ```bash
  make docker-up
  ```

### 4. Create a Django superuser
```bash
make create-superuser
```

### 5. Access
- API: http://localhost:8000/api/
- Admin: http://localhost:8000/admin/

## Deployment Modes
- **test/dev**: Uses SQLite (default)
- **prod**: Uses PostgreSQL (set `ENV=prod` and configure DB env vars)

Switch modes by setting the `ENV` variable in Makefile commands.

## Database Reset
```bash
make reset-db ENV=dev   # For SQLite
docker compose exec nistai make reset-db ENV=prod   # For PostgreSQL
```

## Project Structure
- `govern/`, `map/`, `measure/`, `management/`: Django apps for NIST AI RMF core functions
- `nistaiapp/`: Django project settings and URLs
- `Dockerfile`, `docker-compose.yml`: Containerization
- `Makefile`: Common tasks and automation

## Documentation
See `docs/nist.ai.100-1.pdf` for the NIST AI RMF reference.

## License

This project is licensed under the [GNU Affero General Public License v3.0 (AGPLv3)](https://www.gnu.org/licenses/agpl-3.0.html).

[![AGPLv3 license](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0.html)

