# Raspberry Pi SHT31 sensor test

# Base is official python image https://hub.docker.com/_/python/
FROM python:3-slim
MAINTAINER Asgaut Eng <asgaut@gmail.com>

RUN pip3 install smbus2
COPY sht31.py /

CMD ["python3", "/sht31.py"]
