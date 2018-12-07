import requests
import json
def getData(address, checkDupli = False): #Name of thing to get data from, check if data is duplicate from previous defaults to False
  #checks for data for a certain address or "thing" then makes sure it has not been already sent
  curr = 1
  def updateInfo():
    myUrl = "https://dweet.io/get/latest/dweet/for/" + serv
    myDat = requests.get(myUrl)
    thisJson = json.loads(myDat.text)
    try:
      myMess= thisJson["with"][0]["content"]["myData"]
    except:
      pass
    try:
      return myMess
    except:
      pass
  serv = address
  if(checkDupli == True):
    if curr == 1:
      lastOp = updateInfo()
      curr = curr + 1
    currOp = updateInfo()
    if(currOp == None):
      pass
    else:
      if(lastOp == currOp):
        pass
      else:
        return currOp
      lastOp = currOp
  else:
    thisData = updateInfo()
    return thisData
def sendData(address, data):
    url = "https://dweet.io/dweet/for/" + address + "?myData="+ data
    requests.get(url)
