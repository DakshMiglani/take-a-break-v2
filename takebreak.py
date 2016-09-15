import webbrowser
import time
totalBreaks = 3
takenBreaks = 0

while(takenBreaks < totalBreaks):
    time.sleep(60*60*2)
    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    takenBreaks + 1
    print("The link was opened on " + time.ctime() + "This program was made of A Shah.")
