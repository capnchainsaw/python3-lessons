FROM debian:stretch
MAINTAINER  James Johnson <tiasdungeon@gmail.com>

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3

ADD . /app/
WORKDIR /app/

ENTRYPOINT ["/bin/bash"]
