# -*- coding: utf-8 -*-
import sys,tkinter,pdb,os,cv2
from tkinter import filedialog
import puzl

root=tkinter.Tk()
root.title("karakuri")
root.geometry("600x400")

def helper(event):
	cap = cv2.VideoCapture("mihon.mp4")
	if not cap.isOpened():
		sys.exit()
	while True:
		ret, frame = cap.read()
		if ret:
			cv2.imshow("操作方法", frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		elif cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cv2.destroyWindow("操作方法")

def select_pic(event):
	file_type=[("画像ファイル","*.jpg"),("画像ファイル","*.png"),("画像ファイル","*.bmp")]
	if os.name=="posix":
		directory="/home/"
	elif os.name=="nt":
		directory="c:\\"
	#askopenfilename 一つのファイルを選択する。
	filename=filedialog.askopenfilename(filetypes=file_type,initialdir=directory) 
	root.destroy()
	if not(len(filename)==0): 
		start=puzl.Game(filename)
		start.maingame()

##main##

label = tkinter.Label(root, text="からくり(仮)", font=("",20))
label.pack()

b_sel_pic=tkinter.Button(text="画像を選ぶ")
b_sel_pic.bind("<Button-1>",select_pic)
b_sel_pic.place(x=300,y=200)

b_help=tkinter.Button(text="操作方法")
b_help.bind("<Button-1>",helper)
b_help.place(x=300,y=250)

root.mainloop()
