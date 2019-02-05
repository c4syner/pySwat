from gsearch.googlesearch import search
import webbrowser
def searchError(myError):
  print(myError)
  print("Error found, searching for solution...\n\n\n\n")
  thisSearch = search(myError)
  thisUrl = thisSearch[0][1]
  print(thisUrl)
  webbrowser.open(thisUrl)