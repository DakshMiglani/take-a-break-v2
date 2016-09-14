import webbrowser
import time
totalBreaks = 10
takenBreaks = 0

while(takenBreaks < totalBreaks):
    time.sleep(60*60*2)
    webbrowser.open_new("https://www.youtube.com/watch?v=9_IWRuryzaY")
    takenBreaks + 1
    print("The link was opened on " + time.ctime() + "This program was made of A Shah.")
