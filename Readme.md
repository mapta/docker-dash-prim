# About

This is a simple demo for a [Dash](https://plotly.com/dash/) application deployed as a web app from a Docker image on Azure. 

The deployment is automated with the Azure command line tools (CLI). A new resource group is created and the following resources are deployed:
1. [Azure Container Registry](https://azure.microsoft.com/en-us/services/container-registry/)
2. [Azure App Service Plan](https://docs.microsoft.com/en-us/azure/app-service/overview-hosting-plans)
3. [Azure Web Apps](https://azure.microsoft.com/en-us/services/app-service/web/)
4. [Webhook](https://docs.microsoft.com/en-us/azure/container-registry/container-registry-webhook)

The web app pulls the Docker image from the container registry and if deployment is successful can be reached at **[docker-dash-prim.azurewebsites.net](https://azure.microsoft.com/en-us/resources/videos/azure-appservice-overview/)**. 

Continuous deployment is enabled for the web app and a webhook is created to pull the most recent version of the Docker container if any changes are registered.

[Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) needs to be installed when running from a local machine. Alternatively, Azure Cloud Shell can be used for deployment which has the CLI preinstalled.
The VSCode [Azure CLI Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azurecli) extension can be used to work with the deployment commands with IntelliSense and his highly recommended.

A system-assigned [managed identity](https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/overview) is used for the web app to access the container registry. Thereby, secure communication is ensured without having to manage credentials in the application.

## Build and run Docker locally

```bash
docker build -t app:latest .
docker run -p 8050:8050 app
```

## Deploy the Application on Azure

```bash
bash deploy.azcli
```

## Update the Container Image

```bash
bash build.azcli
```

## Remove all Resources
```bash
az group delete --name $resourceGroupName
```

## References
- [Docker-Dash](https://github.com/jucyai/docker-dash/blob/master/Dockerfile)
- [Webhook](https://medium.com/@ashokduddukuri/continuous-deployment-with-azure-web-app-and-containers-for-your-private-apps-b9b90d4fb8cd)
- [Primes](https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188)

>