FROM python:3.11-slim-buster
RUN apt-get -y update
RUN apt-get -y install curl wget libxrender1 libxext6 fontconfig libjpeg62-turbo xfonts-base xfonts-75dpi
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.buster_amd64.deb
RUN dpkg --install wkhtmltox_0.12.5-1.buster_amd64.deb

RUN apt-get -y install gdal-bin

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
	cd /usr/local/bin && \
	ln -s /opt/poetry/bin/poetry && \
	poetry config virtualenvs.create false

WORKDIR /code

# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml .
COPY poetry.lock .

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=true

# RUN poetry install -E psycopg2 -E gdal --no-dev
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

# COPY ./app /app
ENV PYTHONPATH=/code

COPY . .


CMD ["python", "manage.py", "runserver"]
