\# Thumbnail Micro-Service

FastAPI + Pillow – POST an image URL → receive base64 thumbnail.



\## Run

docker compose up --build

curl -X POST http://localhost:8000/thumb -H "Content-Type: application/json" -d '{"url":"https://via.placeholder.com/600"}'

