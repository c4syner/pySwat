import requests
import json
class Stonesthrow:
  def getData(address, itemIndex): #Name of thing to get data from
    #checks for data for a certain address or "thing" then makes sure it has not been already sent
    curr = 1
    def updateInfo(serv, itemDex):
      myUrl = "https://dweet.io/get/latest/dweet/for/" + serv
      myDat = requests.get(myUrl)
      thisJson = json.loads(myDat.text)
      try:
        myMess= thisJson["with"][0]["content"][itemDex]
      except:
        pass
      try:
        return myMess
      except:
        pass
    thisData = updateInfo(address, itemIndex)
    return thisData
  def sendData(address, data, itemIndex):
      url = "https://dweet.io/dweet/for/" + address + "?" + itemIndex+ "="+ data
      requests.get(url)
