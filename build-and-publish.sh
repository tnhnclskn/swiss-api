docker build . \
    --arch amd64 \
    --tag docker.io/tnhnclskn/swiss-api

docker push docker.io/tnhnclskn/swiss-api:latest