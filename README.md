# Stonesthrow
A rudimentary peer-to-peer API for sending slow data between devices.

## Installation
```bash
pip3 install stonesthrow
```

## Usage
Example: 
```python
from stonesthrow import stonesthrow
server = "anything" #make a server address
data = "Data I want to send"
jsonObj = "objLoc" #Json object where data will be stored
stonesthrow.sendData(server, data, jsonObj) #Send data to specified address
myResp = stonesthrow.getData(server, jsonObj) # Get data from specified address and specified json variable
print(myResp) # Print data found

```
 
 

