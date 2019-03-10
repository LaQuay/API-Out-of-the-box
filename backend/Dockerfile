FROM python:3.7.2-alpine3.9

ENV API_DIR /opt/api/

COPY requirements ./requirements/

ENV HOME /root

# Install psycopg2 requirements
RUN apk add postgresql-dev gcc python3-dev musl-dev

# Install requirements
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements/dev.txt

# removing credentials
RUN rm -r requirements

RUN mkdir -p $API_DIR/source/
WORKDIR $API_DIR

COPY source $API_DIR/source/
ENV PROJECT_ROOT $API_DIR/source/

COPY tests $API_DIR/tests/
# COPY .coveragerc $API_DIR/
# COPY pytest.ini $API_DIR/
COPY scripts $API_DIR/scripts/
COPY scripts /usr/bin

RUN mkdir -p $API_DIR/reports

EXPOSE 5000
WORKDIR $PROJECT_ROOT
CMD ["run.sh"]