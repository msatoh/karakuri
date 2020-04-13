import sys,tkinter
from tkinter import messagebox
from tkinter import filedialog

root=tkinter.Tk()
root.title("karakuri")
root.geometry("600x400")

def select_pic(event):
	file_type=[("画像","*.jpg")]
	directory="/home/"
	#askopenfilename 一つのファイルを選択する。
	filename=filedialog.askopenfilename(filetypes=file_type,initialdir=directory) 
	messagebox.showinfo('FILE NAME is ...',filename)


button=tkinter.Button(text="画像を選ぶ")
button.bind("<Button-1>",select_pic)
button.place(x=300,y=200)

root.mainloop()