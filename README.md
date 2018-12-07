# Stonesthrow
A rudimentary peer-to-peer API for sending slow data between devices.

## Installation
```bash
pip install stonesthrow
```

## Usage
Example: 
```python
from stonesthrow import Stonesthrow
server = "anything" #make a server address
data = "Data I want to send"
myComms = Stonesthrow # Make a networking object
myComms.sendData(server, data) #Send data to specified address
myResp = myComms.getData(server) # Get data from specified address
print(myResp) # Print data found

```
 
 

