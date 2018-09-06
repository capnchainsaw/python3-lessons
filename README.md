# python3-lessons
Sample Python 3 code run in Docker environments
```
docker build -t capnchainsaw/python3-lessons .
docker run -v $(pwd)/scripts:/app -it capnchainsaw/python3-lessons:latest
```
Volume mount in command allows for development without reloading the container.
