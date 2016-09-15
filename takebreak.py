import webbrowser
import time
totalBreaks = 3
takenBreaks = 0

while(takenBreaks < totalBreaks):
    takenBreaks = takenBreaks + 1
    time.sleep(3)
    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


print("The link was opened on " + time.ctime() + "This program was made of A Shah.")
if(takenBreaks == totalBreaks):
        print("The Program has finished the work.")
