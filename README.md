# API-Out-of-the-box

Run your API out of the box, simple and easy. All the software included is Open Source.

## Requirements

- Docker
- Docker compose

## Setup
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