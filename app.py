''' to get the history of your downloads open links.pkl '''

from pytube import YouTube
import re
import tkinter as tk
from tkinter import filedialog
import pickle
from datetime import datetime

def remove_special_characters(text):
    pattern = r'[^a-zA-Z0-9\s]'
    clean_text = re.sub(pattern, '', text)
    
    return clean_text


def read_path():    
    with open("./directory.pkl", "rb") as file:    
        unpickled_string = pickle.loads(file.read())
        return unpickled_string


def get_video(lnk, n):
    
       
    if n == 1:   
        
        
        yt = YouTube(lnk)   
        title= remove_special_characters(yt.title)+".mp4"
    
        print("downloading ", title)    
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # Download the video
        try:
            
            # print(title)
            
            # print(f"{read_path()}/{title}.mp4")
    
            stream.download(filename=title, output_path=read_path())    
            print("downloaded ", title, "\n")    
        except Exception as e1:
            stream.download(filename=f"{str(title)}.mp4", output_path=read_path())    
            print("downloaded ", title, "\n")    

            
    else:
        c= 0 
        for i in lnk:
            c+=1
            
            yt = YouTube(i)   
            title= yt.title
        
            print("downloading ",c, title)    
            
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        # Download the video
            stream.download(filename=f"{title}.mp4", output_path=read_path())    
            print("downloaded ", c,title, "\n")    
        


# # Example data



def store_url(p1):     
    current_time = datetime.now()
    
    with open("./links.pkl", "rb") as f:
        
        existing_data = pickle.load(f)
    
    existing_data.extend([{str(current_time):[p1]}])


    with open("./links.pkl", "wb") as f:
        pickle.dump(existing_data, f)
    
        
    
 
        
def store_path(p):   
    string_pickled = pickle.dumps(p)
    with open("directory.pkl", "wb") as file:    
        file.write(string_pickled)
    
        
    
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

    


urls = []
try:
    qty = int(input("number of videos-     -"))
    if qty == 1:
        link = input("enter youtube url-    -")
        # store the video url - 
        get_video(link, qty)
        # store_url(link)
    else:
        for i in range(qty):
            
            link = input("enter youtube url-    -")
            urls.append(link)
            
        get_video(urls, qty)
        # store_url(urls)
    
except Exception as e:     print("you entered something wrong ", e)