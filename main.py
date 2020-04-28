# -*- coding: utf-8 -*-
import sys,tkinter,os,cv2,pygame,random#,pdb
from tkinter import filedialog
import puzl
from lib import cv_util

root=tkinter.Tk()
root.title("karakuri")
root.geometry("600x400")

def helper(event):
	cap = cv2.VideoCapture("src/mihon.mp4")
	if not cap.isOpened():
		sys.exit()
	while True:
		ret, frame = cap.read()
		if ret:
			cv2.imshow("操作方法", frame)
			if cv2.waitKey(30) & 0xFF == ord('q'):
				break
			elif not cv_util._is_visible("操作方法"):
				break
		elif cv2.waitKey(30) & 0xFF == ord('q'):
			break
		elif not cv_util._is_visible("操作方法"):
			break

	cv2.destroyWindow("操作方法")



def select_pic(event):
	pygame.mixer.music.stop()
	pygame.mixer.music.load("src/MusMus-BGM-065.mp3")
	pygame.mixer.music.play(-1)
	file_type=[("画像ファイル","*.jpg"),("画像ファイル","*.png"),("画像ファイル","*.bmp")]
	if os.name=="posix":
		directory="/home/"
	elif os.name=="nt":
		directory="c:\\"
	if event.widget==b_exer_mode:
		mode="exercise"
		#askopenfilenames 複数ファイルを選択する。
		filenames=filedialog.askopenfilenames(filetypes=file_type,initialdir=directory) 
		if not(len(filenames)==0): 
			root.destroy()
			while True:
				start=puzl.Game(filenames[random.randint(0,len(filenames)-1)])
				if start.maingame(mode)=="end":
					break
	elif event.widget==b_endl_mode:
		mode="endless"
		#askopenfilename 一つのファイルを選択する。
		filename=filedialog.askopenfilename(filetypes=file_type,initialdir=directory) 
		if not(len(filename)==0): 
			root.destroy()
			start=puzl.Game(filename)
			start.maingame(mode)

##main##

pygame.mixer.init()
pygame.mixer.music.load("src/MusMus-BGM-093.mp3")
pygame.mixer.music.play(-1)

label = tkinter.Label(root, text="からくり(仮)", font=("",20))
label.grid(row=0, padx=5, pady=50)

b_exer_mode=tkinter.Button(text="エクササイズモード")
b_exer_mode.bind("<Button-1>",select_pic)
b_exer_mode.grid(row=5, padx=200, pady=10,ipadx=10,sticky=tkinter.W + tkinter.E)

b_endl_mode=tkinter.Button(text="エンドレスモード")
b_endl_mode.bind("<Button-1>",select_pic)
b_endl_mode.grid(row=6, padx=200, pady=10,ipadx=10,sticky=tkinter.W + tkinter.E)

b_help=tkinter.Button(text="操作方法")
b_help.bind("<Button-1>",helper)
b_help.grid(row=8, padx=200, pady=100,ipadx=10,sticky=tkinter.W + tkinter.E)

root.mainloop()
