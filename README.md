# Docker image for simple test of SHT31 sensor on Raspberry Pi 2/3

## Building

```sh
$ docker build -t sht31-test .
```

## Running

```sh
$ docker run --rm --device /dev/i2c-1 sht31-test
```

This runs python3 sht31.py inside a container and prints the measurements:

```
Temperature in Celsius is: 26.68 C
Temperature in Fahrenheit is: 80.02 C
Relative Humidity is: 42.33 %RH
```
