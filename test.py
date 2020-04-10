# coding:UTF=8

# from PIL import Image
import numpy,math
import pdb,sys,time,cv2
#import tkinter
#import pyautogui


class Mouse():
	def __init__(self):
		self.x_hold=0
		self.y_hold=0
		self.hold=False
		self.buf=numpy.zeros((20,20,3),numpy.uint8)
	def mouse_event(self,event,x,y,flags,param):
		if event==cv2.EVENT_LBUTTONDOWN:
			self.x_hold=x
			self.y_hold=y
		elif event==cv2.EVENT_MOUSEMOVE and self.x_hold!=0 and self.y_hold!=0 and self.hold==False:
			if flags==cv2.EVENT_FLAG_LBUTTON:
				if x-self.x_hold>10:
					print("→")
					for i in range(1,20,1):
						for j in range(1,20,1):
							self.buf[i][j]=white_canvas_array[math.floor((y-1)/20)*20+i][canvas_width-20+j]
					for i in range(1,20,1,):
						for j in range(canvas_width,20,-1):
							white_canvas_array[math.floor((y-1)/20)*20+i][j-1]=white_canvas_array[math.floor((y-1)/20)*20+i][j-20]
					for i in range(1,20,1):
						for j in range(1,20,1):
							white_canvas_array[math.floor((y-1)/20)*20+i][j]=self.buf[i][j]
					self.hold=True
				elif x-self.x_hold<-10:
					print("←")
					self.hold=True
				elif y-self.y_hold<-10:
					print("↑")
					self.hold=True
				elif y-self.y_hold>10:
					print("↓")
					self.hold=True
		elif event==cv2.EVENT_LBUTTONUP:
			self.hold=False

img=cv2.imread("e6af7755-s.jpg",1)
cv2.namedWindow("img",cv2.WINDOW_NORMAL)

mouse_t=Mouse()

canvas_height=img.shape[0]+200
canvas_width=img.shape[1]+200
print(canvas_height,canvas_width)

white_canvas_array=numpy.full((canvas_height,canvas_width,3),255,numpy.uint8)

#周りを白埋め
for i in range(0,img.shape[0],1):
	for j in range(0,img.shape[1],1):
		white_canvas_array[i+100][j+100]=img[i][j]

cv2.setMouseCallback("img",mouse_t.mouse_event)

#'q'が押されたら終了
while(True):
	cv2.imshow("img",white_canvas_array)
	if cv2.waitKey(1) & 0xff==ord("q"):
		break
cv2.destroyAllWindows()