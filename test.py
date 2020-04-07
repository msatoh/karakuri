# coding:UTF=8

# from PIL import Image
# import numpy
import pdb,sys,time,cv2
#import tkinter
#import pyautogui


class Mouse():
	def __init__(self):
		self.x_hold=0
		self.y_hold=0
		self.hold=False
	def mouse_event(self,event,x,y,flags,param):
		if event==cv2.EVENT_LBUTTONDOWN:
			self.x_hold=x
			self.y_hold=y
			#self.hold=True
			#cv2.circle(img,(x,y),50,(0,0,255),-1)
		elif event==cv2.EVENT_MOUSEMOVE and self.x_hold!=0 and self.y_hold!=0 and self.hold==False:
			#print(self.x_hold,self.y_hold,x,y)
			if flags==cv2.EVENT_FLAG_LBUTTON:
				if x-self.x_hold>10:
					print("→")
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

cv2.setMouseCallback("img",mouse_t.mouse_event)

while(True):
	cv2.imshow("img",img)
	if cv2.waitKey(1) & 0xff==ord("q"):
		break

cv2.destroyAllWindows()