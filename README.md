# Async-Fair

# Simple Flask App (Cloud Run Template)

A minimal Flask application with Docker and GitHub Actions deployment to Google Cloud Run.

## What this repo contains
- `app.py` – small Flask app with `/` and `/api/hello`
- `templates/index.html` – simple frontend
- `Dockerfile` – builds a container image
- GitHub Actions workflow to build and deploy to Cloud Run

## Setup (Google Cloud)
1. Create a Google Cloud project: `YOUR-GCP-PROJECT-ID`
2. Enable APIs: Cloud Run, Cloud Build, Container Registry (or Artifact Registry), IAM.
3. Create a service account with `roles/run.admin`, `roles/storage.admin`, `roles/cloudbuild.builds.editor`, `roles/iam.serviceAccountUser`.
4. Generate a JSON key for the service account.

## GitHub Secrets
Add these repo secrets:
- `GCP_SA_KEY` — contents of the service account JSON key
- `GCP_PROJECT` — your GCP project id
- `CLOUD_RUN_SERVICE` — Cloud Run service name (e.g. `simple-flask-app`)

## Deploy
Push to `main`. The GitHub Actions workflow will:
1. Build the container using Cloud Build
2. Push to GCR / Artifact Registry
3. Deploy to Cloud Run

## Local running
```bash
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python app.py
# or run with gunicorn
gunicorn --bind 0.0.0.0:8080 app:app
