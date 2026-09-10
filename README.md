# 03 - Python + Django (Practice Target)

> A tiny, real Django web app with 3 endpoints. It runs as-is - your job is to **Dockerize it, ship it, and run it** the same way you did for TaskBoard.

This is a **deployment practice target**, not a coding exercise. The app already works. Treat it as a black box and answer the **7 DevOps questions** below, then put it through the universal recipe.

---

## The 7 DevOps Questions

| # | Question | Answer for this app |
|---|----------|---------------------|
| 1 | **Language / runtime?** | Python 3.11 (Django 4.2) |
| 2 | **How do you build it?** | `pip install -r requirements.txt` (optionally `python manage.py collectstatic` for prod) |
| 3 | **What's the artifact?** | The source tree + its Python deps (a venv). For prod: a WSGI app (`project.wsgi`) served by gunicorn |
| 4 | **Start command?** | Dev: `python manage.py runserver 0.0.0.0:8000` - Prod: `gunicorn project.wsgi` |
| 5 | **Which port?** | `8000` (configurable via `PORT`) |
| 6 | **Config / secrets?** | Env vars: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` (never hardcode in prod!) |
| 7 | **Health check URL?** | `GET /health` -> `{"status":"ok"}` (use for Docker HEALTHCHECK, K8s probes, load balancers) |

---

## Run it locally

From inside this folder (`03-python-django/`):

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply the initial database migrations (creates db.sqlite3)
python manage.py migrate

# 4. Run the dev server
python manage.py runserver 0.0.0.0:8000
```

Now hit the 3 endpoints (in another terminal):

```bash
curl http://localhost:8000/
# Welcome! This is a Python + Django practice app.

curl http://localhost:8000/health
# {"status": "ok"}

curl http://localhost:8000/api/items
# {"items": [{"id": 1, "name": "Keyboard"}, {"id": 2, "name": "Mouse"}, {"id": 3, "name": "Monitor"}, {"id": 4, "name": "Webcam"}]}
```

### Config via environment variables (12-factor)

The app reads these from the environment, with dev-friendly defaults so it runs out of the box:

| Variable | Default | Notes |
|----------|---------|-------|
| `SECRET_KEY` | a dev placeholder | **Set a real one in production.** |
| `DEBUG` | `false` | Set to `true` for local debugging. |
| `ALLOWED_HOSTS` | `*` | Comma-separated list, e.g. `example.com,localhost`. |
| `PORT` | `8000` | The port you pass to `runserver`/gunicorn. |

Example:

```bash
SECRET_KEY="super-secret" DEBUG=true python manage.py runserver 0.0.0.0:8000
```

---

## Your Practice Mission

Everything below is **your job** - none of it is included here on purpose. Building it *is* the practice. Adapt the matching TaskBoard module; the pattern transfers directly.

- [ ] **Dockerize it (M14)** - Write a `Dockerfile` (base `python:3.11`), `pip install`, run with **gunicorn** (`gunicorn project.wsgi`), `EXPOSE 8000`, add a `HEALTHCHECK` hitting `/health`.
- [ ] **Compose (M15)** - A `docker-compose.yml`. **Stretch:** swap SQLite -> **MySQL** (add a `mysqlclient` dep, point `DATABASES` at the env, add a `db` service).
- [ ] **CI/CD (M17)** - A `Jenkinsfile`: build -> test -> build image -> push -> deploy.
- [ ] **VM / IaC (M13)** - Run it on a **Vagrant**/VirtualBox VM.
- [ ] **Configure (M16)** - Provision the server with **Ansible** (install Python, deps, run gunicorn under systemd).
- [ ] **Kubernetes (M18/M19)** - Deployment + Service + Ingress; use `/health` as your liveness/readiness probe; scale it.
- [ ] **Cloud (M20/M21)** - Live on **AWS** (EC2 + RDS), then provision it all with **Terraform**.
- [ ] ** Deployment Update(Gunicorn)** - Gunicorn dependency added for production deployment.
> 🚫 No `Dockerfile`, `Jenkinsfile`, compose, k8s YAML, or Terraform is included - that's the whole point. You already learned how on TaskBoard. Now prove you can do it on a stack you've never seen.
