# omni-autoclock
A python script with selenium that will be put in a docker image for running clock-in and clock-out automatically.

## Things required
- Docker
- Cloud Service (Azure)
- AzureCLI (optional - we can use cloud shell)

## Python
Please enter your credientials in the python file befofe building docker image

## Azure
Create a container registry 
You will get something like: xxxx.azurecr.io

## Dockerfile
Build your image after you enter your account info in `auto-clocker.py`

Login docker hub & your Azure Container Registry
```
docker login
```
```
docker login xxxx.azurecr.io
```

Build dockerfile as my-autoclocker image
```
docker build -t my-autoclocker . --no-cache
```

Use `docker tag` to retag myautoclocker image
```
docker tag my-autoclocker xxxx.azurecr.io/my-autoclocker
```

Push image to Azure Container Registry
```
docker push xxxx.azurecr.io/my-autoclocker
```

## Azure CLI
After the image is pushed to container registry, we can now create the schedule task

Create cron schedule task for clock in
```
az acr task create --name schedule-auto-clock-in --registry xxxx --schedule "0 1 * * 1-5" --cmd "xxxx.azurecr.io/my-autoclocker" --content /dev/null
```

Create another one for clock out (pick your time)
```
az acr task create --name schedule-auto-clock-out --registry xxxx --schedule "3 10 * * 1-5" --cmd "xxxx.azurecr.io/my-autoclocker" --content /dev/null
```

***Note: Timezone is in UTC***
