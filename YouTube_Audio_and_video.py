from pytube import YouTube
import os

link = "https://youtu.be/B07oDle8Hoo"
youtube_1= YouTube (link)

print(youtube_1.title)
#print(youtube1.thumbnail_url)  #for the thumbnail of youtube vedio using video URL

print("Do you want to download Audio or Video\n")
choice=int(input("Enter 1 for Audio and 2 for Video.."))

if (choice==1):
    # url input from user
    yt = YouTube(str(input("Enter the URL of the video you want to download: \n>> ")))
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
  
    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'
  
    # download the file
    out_file = video.download(output_path=destination)
  
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
  
    # result of success
    print(yt.title + " has been successfully downloaded.")

elif(choice==2):
    videos=youtube_1.streams.filter(only_video=True)

    vid=list(enumerate(videos))

    for i in vid:

        print(i)           #printing the number of pixels the video is present in
    print()
    strm=int(input("Enter:"))
    videos[strm].download()
    print("         !VIDEO IS DOWNLOADED SUCESSFULLY!       ")



