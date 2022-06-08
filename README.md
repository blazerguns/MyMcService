# HTTP Requests — you are (probably) doing it wrong
## Code Example
![Cover Photo](./cover.png)

## Prerequirements
To run the example you need node, yarn, .NET5 and docker installed.

## Compilation
One of the service corebanking_backend needs to be compiled first.
```
dotnet publish -c Release -o out
```

## Installation
The following command will fetch all needed node modules.
```
./setup.sh
```

## Run
To run the project execute:
```
docker-compose up
```

This will run docker-compose file and setup the API server on port 3000. The identity server is not
exposed but you can access restricted data by performing HTTP Parameter Polution.

