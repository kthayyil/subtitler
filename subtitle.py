import os
from win10toast import ToastNotifier

# Generate a list of the srt and vid files in the directory
srtlist = [] #To store the list of .srt files in the directory
vidlist = []
for file in os.listdir():
    if '.srt' in file:
        srtlist.append(file)
    if '.avi' in file or '.mkv' in file or '.mp4' in file:
        vidlist.append(file)

# Now rename the files based on the filename (without extension) of the video
# also keep count of the changes made
changeCount = 0
for srt, vid in zip(srtlist,vidlist):
    vid = os.path.splitext(vid)[0] # Strips the filename from the file
    os.rename(srt,vid + '.srt') # renames the file with an appended '.srt'
    changeCount += 1

# Display a tost notification to let the user know what happened
toaster = ToastNotifier()
toaster.show_toast("Enjoy the binge!",
                   str(changeCount) +    " subtitle files were renamed",
                   duration = 1.5)

# More comments here cause why not
