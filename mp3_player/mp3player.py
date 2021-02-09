from tkinter import *
import pygame
from tkinter import filedialog

root= Tk()
root.title('my mp3 player')
root.iconbitmap('D:\\python\\tkinter\\mp3_player')
root.geometry('500x300')

# initilaisting pygame mixer
pygame.mixer.init()

#add song function
def add_song():
    song = filedialog.askopenfilename(intialdir='audio/',title='choose a song', filetypes=(("mo3 Files", "*.mp3"),))
    song = song.replace("c:/gui/audio/","")
    song=song.replace(".mp3","")

    song_box.insert("End, song")
# creating mp3 player box

song_box = Listbox(root, bg="black", fg="green", width=60)
song_box.pack(pady=20)
#play select song
def play():
    song=song_box.get(ACTIVE)
    song=f'c:/gui/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
# creating stop function
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)
#creating player control button image

back_btn_img =PhotoImage(file='D:\\python\\tkinter\\mp3_player\\back_btn_img.png')
forward_btn_img= PhotoImage(file="D:\\python\\tkinter\\mp3_player\\forward_btn_img.png")
play_btn_img = PhotoImage(file="D:\\python\\tkinter\\mp3_player\\play_btn_img.png")
pause_btn_img = PhotoImage(file="D:\\python\\tkinter\\mp3_player\\pause_btn_img.png")
stop_btn_img = PhotoImage(file='D:\\python\\tkinter\\mp3_player\\stop_btn_img.png')

#create control player frame

conntrol_frame = Frame(root)
conntrol_frame.pack()

# creatoing player control button
back_btn= Button(conntrol_frame, image=back_btn_img,height=20,width=30,borderwidth=0) 
forward_btn=Button(conntrol_frame, image=forward_btn_img,height=20,width=30,borderwidth=0)
play_btn=Button(conntrol_frame, image=play_btn_img,height=20,width=30, borderwidth=0,command=play)
pause_btn =Button(conntrol_frame, image=pause_btn_img,height=20,width=30 ,borderwidth=0)
stop_btn =Button(conntrol_frame, image=stop_btn_img ,height=20,width=30, borderwidth= 0,command=stop)

back_btn.grid(row=0,column=0, pady=0)
forward_btn.grid(row=0,column=1,pady=0)
play_btn.grid(row=0,column=2,pady=0)
pause_btn.grid(row=0,column=3,pady=0)
stop_btn.grid(row=0,column=4,pady=0)





root.mainloop()