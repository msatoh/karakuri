# coding:UTF=8

import numpy,math,random,pygame
import sys,time,cv2,tkinter#,pdb
from tkinter import messagebox

class Game():

	def __init__(self,file_name):

		img=cv2.imread(file_name,1)
		cv2.namedWindow("img",cv2.WINDOW_NORMAL)

		self.canvas_height=img.shape[0]+200
		self.canvas_width=img.shape[1]+200

		self.white_canvas=numpy.full((self.canvas_height,self.canvas_width,3),255,numpy.uint8)
		self.initial_canvas=numpy.full((self.canvas_height,self.canvas_width,3),255,numpy.uint8)

		#周りを白埋め
		for i in range(0,img.shape[0],1):
			for j in range(0,img.shape[1],1):
				self.white_canvas[i+100][j+100]=img[i][j]
				self.initial_canvas[i+100][j+100]=img[i][j]

	def maingame(self,mode,lvl):

		if mode=="exercise" and lvl==0:
			# Tkクラス生成
			root = tkinter.Tk()
			root.geometry('300x200')
			root.title('レベル選択')
			# ラベル
			lbl = tkinter.Label(text='レベル（最小移動回数）を入力してください：')
			lbl.place(x=30, y=50)
			# テキストボックス
			txt = tkinter.Entry(width=15)
			txt.place(x=50, y=70)

			def d_lvl_init():
				self.stat=int(txt.get())
				root.destroy()
			#box
			btn=tkinter.Button(text="決定",command=d_lvl_init)
			btn.place(x=180, y=70)

			root.mainloop()
		else:
			self.stat=lvl


		mouse_t=Mouse(self.canvas_height,self.canvas_width,self.white_canvas,self.stat)
		cv2.setMouseCallback("img",mouse_t.mouse_event)

		pygame.mixer.music.load("src/MusMus-BGM-065.mp3")
		pygame.mixer.music.play(-1)


		while(True):
			cv2.imshow("img",self.white_canvas)
			cv2.putText(self.white_canvas,"level: %d"%self.stat,(self.canvas_width-140,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),thickness=1,lineType=cv2.LINE_8)
			if cv2.waitKey(1) & 0xff==ord("q"):#'q'が押されたら終了
				self.stat=-1
				break
			elif (self.initial_canvas==self.white_canvas).all():#元の絵に戻った時
				if mode=="exercise":
					root = tkinter.Tk()
					root.withdraw()
					pygame.mixer.init()
					pygame.mixer.music.load("src/btn15.mp3")
					pygame.mixer.music.play(0)
					if messagebox.showinfo("正解","おみごと")=="ok":
						root.destroy()
						break
				elif mode=="endless":
					se=pygame.mixer.Sound("src/btn07.wav")
					se.play()
					del mouse_t
					self.stat+=1
					mouse_t=Mouse(self.canvas_height,self.canvas_width,self.white_canvas,self.stat)
					cv2.setMouseCallback("img",mouse_t.mouse_event)

		cv2.destroyAllWindows()

		return self.stat # -1:終了　0:まだ始まってない ≧1:レベル

class Mouse(Game): #基本的にはいじらない。buf_size除く
	RIGHT = 1
	LEFT  = 2
	UP    = 3
	DOWN  = 4

	def __init__(self,canvas_height,canvas_width,white_canvas,shuffle_t):
		self.x_hold=0
		self.y_hold=0
		self.buf=numpy.zeros((21,20,3),numpy.uint8)
		self.canvas_height=canvas_height
		self.canvas_width=canvas_width
		self.white_canvas=white_canvas

		#シャッフル shuffle_t:シャッフル回数.=level
		for i in range(0,shuffle_t,1):
			self.slide_pic(random.randint(1,4),random.randint(100,self.canvas_width-100),random.randint(100,self.canvas_height-100))

		self.hold=False #１回目の手動操作を受け付けるようにするため、シャッフル後に初期化

	def slide_pic(self,direction,x,y):
		if direction==self.RIGHT:
			for i in range(1,21,1):
				for j in range(1,20,1):
					self.buf[i-1][j]=self.white_canvas[math.floor((y-1)/20)*20+i-1][self.canvas_width-20+j]
			for i in range(1,21,1,):
				for j in range(self.canvas_width,20,-1):
					self.white_canvas[math.floor((y-1)/20)*20+i-1][j-1]=self.white_canvas[math.floor((y-1)/20)*20+i-1][j-20]
			for i in range(1,21,1):
				for j in range(1,20,1):
					self.white_canvas[math.floor((y-1)/20)*20+i-1][j]=self.buf[i-1][j]
		elif direction==self.LEFT:
			for i in range(1,21,1):
				for j in range(1,20,1):
					self.buf[i-1][j]=self.white_canvas[math.floor((y-1)/20)*20+i-1][j]
			for i in range(1,21,1,):
				for j in range(20,self.canvas_width,1):
					self.white_canvas[math.floor((y-1)/20)*20+i-1][j-20]=self.white_canvas[math.floor((y-1)/20)*20+i-1][j-1]
			for i in range(1,21,1):
				for j in range(1,20,1):
					self.white_canvas[math.floor((y-1)/20)*20+i-1][self.canvas_width-20+j]=self.buf[i-1][j]
		elif direction==self.UP:
			for i in range(1,20,1):
				for j in range(0,20,1):
					self.buf[i][j]=self.white_canvas[i][math.floor((x-1)/20)*20+j-1]
			for i in range(0,self.canvas_height-20,1,):
				for j in range(0,20,1):
					self.white_canvas[i][math.floor((x-1)/20)*20+j-1]=self.white_canvas[i+20][math.floor((x-1)/20)*20+j-1]
			for i in range(1,20,1):
				for j in range(0,20,1):
					self.white_canvas[self.canvas_height-20+i][math.floor((x-1)/20)*20+j-1]=self.buf[i][j]
		elif direction==self.DOWN:
			for i in range(1,20,1):
				for j in range(0,20,1):
					self.buf[i][j]=self.white_canvas[self.canvas_height-20+i][math.floor((x-1)/20)*20+j-1]
			for i in range(self.canvas_height-20,1,-1,):
				for j in range(0,20,1):
					self.white_canvas[i+19][math.floor((x-1)/20)*20+j-1]=self.white_canvas[i-1][math.floor((x-1)/20)*20+j-1]
			for i in range(1,20,1):
				for j in range(0,20,1):
					self.white_canvas[i][math.floor((x-1)/20)*20+j-1]=self.buf[i][j]			
		self.hold=True		

	def mouse_event(self,event,x,y,flags,param):
		if event==cv2.EVENT_LBUTTONDOWN:
			self.x_hold=x
			self.y_hold=y
		elif event==cv2.EVENT_MOUSEMOVE and self.x_hold!=0 and self.y_hold!=0 and self.hold==False: #マウスの左ボタンが押されたまま動いた時
			print ("move",self.x_hold,self.y_hold,x,y,flags,flags==cv2.EVENT_FLAG_LBUTTON,)
			if flags==cv2.EVENT_FLAG_LBUTTON:
				print("buton")
				if x-self.x_hold>10:
					self.slide_pic(self.RIGHT,x,y)
				elif x-self.x_hold<-10:
					self.slide_pic(self.LEFT,x,y)
				elif y-self.y_hold<-10:
					self.slide_pic(self.UP,x,y)
				elif y-self.y_hold>10:
					self.slide_pic(self.DOWN,x,y)
		elif event==cv2.EVENT_LBUTTONUP:
			self.hold=False
