# -*- coding: utf-8 -*-
import sys,tkinter,os,cv2,pygame,random,pdb
from tkinter import filedialog
from PIL import Image, ImageTk
import puzl
from lib import cv_util

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
	file_type=[("画像ファイル","*.jpg"),("画像ファイル","*.png"),("画像ファイル","*.bmp")]
	if os.name=="posix":
		directory="/home/"
	elif os.name=="nt":
		directory="c:\\"
	if event.widget==b_exer_mode:
		#askopenfilenames 複数ファイルを選択する。
		filenames=filedialog.askopenfilenames(filetypes=file_type,initialdir=directory) 
		if not(len(filenames)==0): 
			root.destroy()

			# Tkクラス生成
			lvl_slct = tkinter.Tk()
			lvl_slct.geometry('300x200')
			lvl_slct.title('レベル選択')
			# ラベル
			lbl = tkinter.Label(text='レベル（移動回数）を入力してください：')
			lbl.place(x=10, y=50)
			# テキストボックス
			txt = tkinter.Entry(width=15)
			txt.place(x=50, y=70)

			def d_lvl_init():
				global level
				level=int(txt.get())
				if level==0:
					level=999
				lvl_slct.destroy()
			#box
			btn=tkinter.Button(text="決定",command=d_lvl_init)
			btn.place(x=180, y=70)

			lvl_slct.mainloop()

			while True: #maingame関数を何回も呼び直すことで実装
				start=puzl.Game(filenames[random.randint(0,len(filenames)-1)])
				if start.maingame("exercise",level)<0:
					break


	elif event.widget==b_endl_mode:
		#askopenfilename 一つのファイルを選択する。
		filename=filedialog.askopenfilename(filetypes=file_type,initialdir=directory) 
		if not(len(filename)==0): 
			root.destroy()
			start=puzl.Game(filename)
			start.maingame("endless",1) #maingame関数内で実装

##main##

pygame.mixer.init()
pygame.mixer.music.load("src/MusMus-BGM-093.mp3")
pygame.mixer.music.play(-1)

root=tkinter.Tk()
root.title("karakuri")
root.geometry("600x400")

label = tkinter.Label(root, text="からくり(仮)", font=("",20))
label.grid(row=0, padx=5, pady=50)

# 画像を指定                                                                    
img = Image.open('src/pose_puzzle_kumiawaseru.png')
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)
# canvasサイズ                          
canv = tkinter.Canvas(width=100, height=100)
canv.place(x=380, y=10)
# -------------------------------------                                         
# キャンバスに画像を表示する                                                    
canv.create_image(0, 0, image=img, anchor=tkinter.NW)

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
