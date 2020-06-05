# -*- coding: utf-8 -*-
import sys,tkinter,os,cv2,pygame,random,pdb,csv
from tkinter import filedialog
from PIL import Image, ImageTk
import puzl,db
from lib import cv_util
#from functools import partial --ウィジェット選択時の関数に引数を与える

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
			# elif not cv_util._is_visible("操作方法"):
			# 	break
		elif cv2.waitKey(30) & 0xFF == ord('q'):
			break
		# elif not cv_util._is_visible("操作方法"):
		# 	break

	cv2.destroyWindow("操作方法")

def disp_ranking(event):

	def end_end():
		d_rank.destroy()
		pygame.mixer.music.stop()
		pygame.mixer.music.load("src/MusMus-BGM-093.mp3")
		pygame.mixer.music.play(-1)

	d_rank=tkinter.Tk()
	d_rank.geometry("400x300")
	d_rank.title("ランキング")
	pygame.mixer.music.load("src/MusMus-BGM-019.mp3")
	pygame.mixer.music.play(-1)

	disp_r=[[]*2]*5
	r=db.fileoc("","-1")
	i=0
	for cnt in r:
		disp_r[i]=tkinter.Label(d_rank,text=str(i+1)+"位:\t"+r[i][0]+"\t"+r[i][1], font=("",18))
		disp_r[i].grid(row=i, padx=75, pady=4)
		i+=1
		if i==5:
			break
	#box
	e_end=tkinter.Button(d_rank,text="終了",command=end_end)
	e_end.place(x=180,y=240)

	d_rank.mainloop()

def f_result(sc):
	pygame.mixer.music.stop()
	fanfare=pygame.mixer.Sound("src/ファンファーレ4.wav")
	fanfare.play()
	w_result = tkinter.Tk()
	w_result.geometry('400x300')
	w_result.title('スコア')
	# ラベル
	scr = tkinter.Label(text="あなたのスコアは"+str(sc)+"です！",font=("",20))
	scr.place(x=10, y=40)
	enter_name = tkinter.Label(text="entry your name:")
	enter_name.place(x=10, y=80)
	t_name = tkinter.Entry(width=15)
	t_name.place(x=150, y=80)
	def ok_end():
		d_name=t_name.get()
		w_result.destroy()#d_nameを取得してから画面を消す
		db.fileoc(str(d_name),str(sc))
		disp_ranking(0)
	#box
	b_end=tkinter.Button(text="終了",command=ok_end)
	b_end.place(x=200,y=120)
	w_result.mainloop()

def level_select():
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

			level_select()

			score=0
			while True: #maingame関数を何回も呼び直すことで実装
				start=puzl.Game(filenames[random.randint(0,len(filenames)-1)])
				if start.maingame(score,level)<0:
					break
				else:
					score+=1

	elif event.widget==b_endl_mode:
		#askopenfilename 一つのファイルを選択する。
		filename=filedialog.askopenfilename(filetypes=file_type,initialdir=directory) 
		if not(len(filename)==0): 
			root.destroy()
			start=puzl.Game(filename)
			f_result(start.maingame(-1,1)) #maingame関数内で実装

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

b_rank=tkinter.Button(text="ランキング")
b_rank.bind("<Button-1>",disp_ranking)
b_rank.grid(row=7, padx=200, pady=30,ipadx=10,sticky=tkinter.W + tkinter.E)

b_help=tkinter.Button(text="操作方法")
b_help.bind("<Button-1>",helper)
b_help.grid(row=8, padx=200, pady=0,ipadx=10,sticky=tkinter.W + tkinter.E)

root.mainloop()
