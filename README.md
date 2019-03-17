# API-Out-of-the-box
Run your API out of the box, and consume it, simple, fast and easy. 

Have you ever wanted to perform a proof of concept in which you needed backend software and frontend software? 
Or, have you ever seen the need to start a project but did not know where?

In this repository you will find code and information on how to start from almost-zero a project that has a backend, frontend, and an Android application!

## What includes
#### Backend
- Alpine 3.9
- Python 3.7.2
- Flask 1.0.2

#### Database
- Alpine
- Postgres 11.2
- pgAdmin4.3 

#### Frontend
- Alpine
- React 16.8
- Node 8.15

#### Android application
Based in Android API 28 and with SDK minimum of API 19. It has [Volley](https://developer.android.com/training/volley) ready to be used, to call APIs.

## Requirements
The software is meant to be run with Docker.

- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

And, for the Android App, you need an IDE (e.g. [Android Studio](https://developer.android.com/studio)) and an Android Device.

## Setup

#### Backend
Add your frontend URL in `backend/source/resources_loader.py`

#### Frontend
Add your backend URL in `frontend/src/config.js`

### Run the project!
Run separately.
- `make setup`
- `make run-backend`
- `make run-frontend`

And you will have running in:
- PORT 3000: React - Frontend
- PORT 5000: Flask REST API - Backend
- PORT 5432: PostgresDB
- PORT 5433: pgAdmin 4

### Connect to pgAdmin 4
Open `localhost:5433`. The user and password are the ones that are shown in the `docker-compose.yml`.

To connect to the postgres database. Click in `Add New Server` and add the following information
in the `Connection` tab:

```bash
Host name/address: postgres
Port: 5432
Maintenance database: postgres
Username: postgres
Role:
Service:
```

## Troubleshooting

### Make run failed
Make sure the user has permission to run `run.sh` and that this file is in `LF` format. 

```bash
docker run '...'
standard_init_linux.go:207: exec user process caused "no such file or directory"
Makefile:18: recipe for target 'run' failed
make: *** [run] Error 1
```

### Illegal option '-' in .sh
Make sure the user has permission to run `configure-postgres.sh` and that this file is in `LF` format. 
