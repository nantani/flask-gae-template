docker build -t ml-api .
docker run -rm -it -p 127.0.0.1:8080:8080 ml-api
