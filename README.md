# omni-autoclock
A python script with selenium that will be put in a docker image for running clock-in and clock-out automatically.

## Things required
- Docker
- Cloud Service (Azure)
- AzureCLI

## Python
Please enter your credientials in the python file befofe building docker image

## Dockerfile
Build your image after you enter your account info in `auto-clocker.py`

`docker build -t my-autoclocker . --no-cache`
