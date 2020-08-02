from pytube import YouTube
import sys

link = input("Paste the link: ")
while True:
    try:
        yt = YouTube(link)
        break
    except KeyError:
        print("Resources cannot be collected... ")
        sys.exit("This file cannot be downloaded")
        

print("Title: ", yt.title)
print("Lengths: ", yt.length)

ys = yt.streams.get_highest_resolution()

print("Collecting resources....")

ys.download()
ys.download('/home/senjufy/Desktop/')

print("Downloading. Please wait...")

print("Download Complete!")