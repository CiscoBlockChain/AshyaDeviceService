# AshyaCollector 
here is the implementation of the web-service for the nodes (back-end)

## Build

```
docker build -t ashya/collector . 
```

## Run

```
docker run -it -p 5050:5050 ashya/collector
```

## API

### ```/contract```

#### GET
Gets the current contract address from the database: 
```{ "address" : "0x0d...."}```

#### POST
Write's the current contract address to the database:

```{"address" : "0x0d..."}```

##### Example 

```
curl -X POST -d '{"address" : "0x0343fef"}' -H "Content-Type: application/json"  localhost:5050/contract
```


### ```/urls```

#### GET
Get's the current URLS that the contract is sending data to. The URLS are gathered by reading the data from the contract that is on the blockchain. 