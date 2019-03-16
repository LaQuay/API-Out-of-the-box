# API-Out-of-the-box

Run your API out of the box, simple and easy. 

This is a boilerplate from which you can start a full-stack project.

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
*Work in progress*

## Requirements

- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Setup

### Run the project!
- make build
- make run

And you will have running in:
- PORT 5000: Flask REST API
- PORT 5432: PostgresDB
- PORT 5433: pgAdmin 4

### Connect to pgAdmin 4
Open `localhost:5433`. The user and password are the ones that are shown in the `docker-compose.yaml`.

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
