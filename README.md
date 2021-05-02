# Big Data - NoSQL and Docker Assignemnt
**MSc Princpiples of Data Science**

## To tag and upload a new version of the image

```bash
$ cd twitter
$ docker build -t twitter .
$ docker images
# Identify image hash
$ docker tag <hash> nerucius/twitter:latest
$ docker push nerucous/twitter
```

Please log into docker hub first:
```bash
$ docker login
```

## To run the twitter streamer:

1. `docker compose up -d`
1. Open the browser at `http://localhost:8081/` to view the tweets under the `twitter/corona` collection
1. Can terminate the image at any time with `docker compose down`
1. Default `docker-compose.yaml` file will create a persisten volume for mongodb storage.
1. The app wil auto-shutdown at 100 tweets recorded so API limits are not exceded
