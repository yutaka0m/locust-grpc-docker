FROM python:3.9

WORKDIR /build
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --deploy && \
    pip uninstall -y pipenv virtualenv-clone virtualenv

RUN useradd --create-home locust
WORKDIR /home/locust

USER locust
ENTRYPOINT ["locust"]
EXPOSE 8089 5557
