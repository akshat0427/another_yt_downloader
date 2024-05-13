from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import pickle


def store_path(p):   
    string_pickled = pickle.dumps(p)
    with open("directory.pkl", "wb") as file:    
        file.write(string_pickled)
        
def read_path():    
    with open("./directory.pkl", "rb") as file:    
        unpickled_string = pickle.loads(file.read())
        return unpickled_string
    
def get_directory_path():
    root = tk.Tk()
    root.withdraw()
    directory_path = filedialog.askdirectory(
        title="where to save",
        initialdir=read_path()  # Default directory
    )
    if directory_path:
        return directory_path
    else:
        return None

'''  wake them when the specified file needs to be saved in a new directory '''
# d_path = get_directory_path()
# store_path(d_path)


urls = ["https://www.youtube.com/watch?v=rdyxkUglFR0","https://www.youtube.com/watch?v=_qAL3rpQLa4",  "https://www.youtube.com/watch?v=JkiFuUUoDOg", "https://www.youtube.com/watch?v=ov6-wfN0I7s"]



c = 0
for i in urls:  
    
    yt = YouTube(i)   
    title= yt.title
    c+=1
    
    print("downloading ", title, c)    
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Download the video
    stream.download(filename=f"{title}.mp4", output_path=read_path())    
    print("downloaded ", title, c, "\n")    