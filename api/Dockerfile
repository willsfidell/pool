FROM python:3.10.4-alpine

ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./

RUN \
  apk add --no-cache build-base && \ 
  apk add --no-cache --virtual .build-deps gcc musl-dev && \
  python -m pip install -r requirements.txt --no-cache-dir && \
  apk --purge del .build-deps

COPY . .

ENV PYTHONPATH="."

CMD ["python", "app/main.py"]   
#ENTRYPOINT /bin/sh
