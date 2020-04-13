# coding:UTF=8

# from PIL import Image
import numpy,math
import pdb,sys,time,cv2
#import tkinter
#import pyautogui

class Game():
	def maingame(self,filename):
		img=cv2.imread(filename,1)
		cv2.namedWindow("img",cv2.WINDOW_NORMAL)

		self.canvas_height=img.shape[0]+200
		self.canvas_width=img.shape[1]+200
		#print(self.canvas_height,self.canvas_width)

		self.white_canvas_array=numpy.full((self.canvas_height,self.canvas_width,3),255,numpy.uint8)

		#周りを白埋め
		for i in range(0,img.shape[0],1):
			for j in range(0,img.shape[1],1):
				self.white_canvas_array[i+100][j+100]=img[i][j]

		mouse_t=Mouse(self.canvas_height,self.canvas_width,self.white_canvas_array)
		cv2.setMouseCallback("img",mouse_t.mouse_event)

		#'q'が押されたら終了
		while(True):
			cv2.imshow("img",self.white_canvas_array)
			if cv2.waitKey(1) & 0xff==ord("q"):
				break

		cv2.destroyAllWindows()

class Mouse(Game):
	def __init__(self,canvas_height,canvas_width,white_canvas_array):
		self.x_hold=0
		self.y_hold=0
		self.hold=False
		self.buf=numpy.zeros((21,20,3),numpy.uint8)
		self.canvas_height=canvas_height
		self.canvas_width=canvas_width
		self.white_canvas_array=white_canvas_array
	def mouse_event(self,event,x,y,flags,param):
		if event==cv2.EVENT_LBUTTONDOWN:
			self.x_hold=x
			self.y_hold=y
		elif event==cv2.EVENT_MOUSEMOVE and self.x_hold!=0 and self.y_hold!=0 and self.hold==False:
			if flags==cv2.EVENT_FLAG_LBUTTON:
				if x-self.x_hold>10:
					#print("→")
					for i in range(1,21,1):
						for j in range(1,20,1):
							self.buf[i-1][j]=self.white_canvas_array[math.floor((y-1)/20)*20+i-1][self.canvas_width-20+j]
					for i in range(1,21,1,):
						for j in range(self.canvas_width,20,-1):
							self.white_canvas_array[math.floor((y-1)/20)*20+i-1][j-1]=self.white_canvas_array[math.floor((y-1)/20)*20+i-1][j-20]
					for i in range(1,21,1):
						for j in range(1,20,1):
							self.white_canvas_array[math.floor((y-1)/20)*20+i-1][j]=self.buf[i-1][j]
					self.hold=True
				elif x-self.x_hold<-10:
					#print("←")
					for i in range(1,21,1):
						for j in range(1,20,1):
							self.buf[i-1][j]=self.white_canvas_array[math.floor((y-1)/20)*20+i-1][j]
					for i in range(1,21,1,):
						for j in range(20,self.canvas_width,1):
							self.white_canvas_array[math.floor((y-1)/20)*20+i-1][j-20]=self.white_canvas_array[math.floor((y-1)/20)*20+i-1][j-1]
					for i in range(1,21,1):
						for j in range(1,20,1):
							self.white_canvas_array[math.floor((y-1)/20)*20+i-1][self.canvas_width-20+j]=self.buf[i-1][j]
					self.hold=True
				elif y-self.y_hold<-10:
					#print("↑")
					for i in range(1,20,1):
						for j in range(0,20,1):
							self.buf[i][j]=self.white_canvas_array[i][math.floor((x-1)/20)*20+j-1]
					for i in range(0,self.canvas_height-20,1,):
						for j in range(0,20,1):
							self.white_canvas_array[i][math.floor((x-1)/20)*20+j-1]=self.white_canvas_array[i+20][math.floor((x-1)/20)*20+j-1]
					for i in range(1,20,1):
						for j in range(0,20,1):
							self.white_canvas_array[self.canvas_height-20+i][math.floor((x-1)/20)*20+j-1]=self.buf[i][j]
					self.hold=True
				elif y-self.y_hold>10:
					#print("↓")
					for i in range(1,20,1):
						for j in range(0,20,1):
							self.buf[i][j]=self.white_canvas_array[self.canvas_height-20+i][math.floor((x-1)/20)*20+j-1]
					for i in range(self.canvas_height-20,1,-1,):
						for j in range(0,20,1):
							self.white_canvas_array[i+19][math.floor((x-1)/20)*20+j-1]=self.white_canvas_array[i-1][math.floor((x-1)/20)*20+j-1]
					for i in range(1,20,1):
						for j in range(0,20,1):
							self.white_canvas_array[i][math.floor((x-1)/20)*20+j-1]=self.buf[i][j]
					self.hold=True
		elif event==cv2.EVENT_LBUTTONUP:
			self.hold=False