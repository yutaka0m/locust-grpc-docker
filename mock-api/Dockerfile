FROM python:3.9-slim-buster

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --deploy && \
    pip uninstall -y pipenv virtualenv-clone virtualenv

COPY *.py /app/

CMD [ "python3", "main.py"]
