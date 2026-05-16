# Deployment Guide

## Google Cloud Run
1. Build the images: `docker build -t gcr.io/PROJECT_ID/backend -f app/Dockerfile .`
2. Push to GCR: `docker push gcr.io/PROJECT_ID/backend`
3. Deploy: `gcloud run deploy backend --image gcr.io/PROJECT_ID/backend`

## Vertex AI
Ensure the service account has `Vertex AI User` permissions.
The system uses `gemini-pro` for reasoning and `text-embedding-004` for vectors.
