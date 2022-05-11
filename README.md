# pool

## Requirements
* Docker, Docker-composer, or Python 3 environment

## To run

I typically use the docker-composer method

### Docker
From `api` directory
```console
$ docker build -t poolio_api .
$ docker run -p 127.0.0.1:8888:8888/tcp poolio_api
```
### Docker-composer
From project root directory 
```console
$ docker-compose up -d 
```

### Python 3 environment
```console
$  uvicorn main:app --reload
```

## API docs

The browser api docs, in swagger format, can be found at http://localhost:8888/docs
From the docs you can test the api calls, they also display the curl commands that be used to test the api from the cli
