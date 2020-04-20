# -*- coding: utf-8 -*-
import sys,tkinter,pdb,os
from tkinter import filedialog
import puz

root=tkinter.Tk()
root.title("karakuri")
root.geometry("600x400")

def select_pic(event):
	file_type=[(u"画像","*.jpg")]
	if os.name=="posix":
		directory="/home/"
	elif os.name=="nt":
		directory="c:\\"
	#askopenfilename 一つのファイルを選択する。
	filename=filedialog.askopenfilename(filetypes=file_type,initialdir=directory) 
	root.destroy()

	start=puz.Game(filename)
	start.maingame()

button=tkinter.Button(text="画像を選ぶ")
button.bind("<Button-1>",select_pic)
button.place(x=300,y=200)

root.mainloop()
