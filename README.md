# Stonesthrow
A rudimentary peer-to-peer API for sending slow data between devices.

## Installation
```bash
pip install stonesthrow
```

## Usage
Example: 
```python
from stonesthrow import stonesthrow
server = "anything" #make a server address
data = "Data I want to send"
stonesthrow.sendData(server, data) #Send data to specified address
myResp = stonesthrow.getData(server) # Get data from specified address
print(myResp) # Print data found

```
 
 

