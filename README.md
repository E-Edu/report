
# Python Flask Report Microservice

View **[Dockerfile](https://github.com/E-Edu/report/blob/master/Dockerfile)** on GitHub.

## Docker image tags

* **Image name:** `eedu/reportms`


## Environment Variables

| Variable         | Required | Default   | Description |
|------------------|----------|-----------| ------------|
| `DATABASE_HOSTNAME` |Yes|  | / |
| `DATABASE_PORT`     |Yes|  | / |
| `DATABASE_USERNAME` |Yes|  | / |
| `DATABASE_PASSWORD` |Yes|  | / |
| `DATABASE_DATABASE` |Yes|  | / |
| `JWT_SECRET`        |Yes|  | / |
| `SERVICE_SECRET`    |Yes|  | / |



### Basic structure

The following is the least required directory structure:
```bash
<project-dir>/
├── app.py				# Entrypoint Development Server
├── wsgi.py				# Entrypoint gunicorn
├─── report                     
│    ├──  Blueprints			# Folder with [Routes]
│    │		├── __init__.py		# Empty File
│    │		├── error_handler.py	# Error Handler z.B. 404
│    │		└── routes.py  		# Default Routes()
│    ├── __init__.py			# Register Blueprints and DB Stuff
│    └── database.py			# DB Stuff
├── requirements.txt			
└── docker-compose.yml			
```

### Run with Docker

```bash
docker run \
  -e DATABASE_HOSTNAME='' \
  -e DATABASE_PORT='' \
  -e DATABASE_USERNAME='' \
  -e DATABASE_PASSWORD='' \
  -e DATABASE_DATABASE='' \
  -e JWT_SECRET='' \
  -e SERVICE_SECRET='' \
  eedu/reportms
```

### Run with docker-compose

For easy usage, there is a Docker Compose example project included.
```bash
docker-compose up -d
```
```bash
curl localhost:80/ticket
```


