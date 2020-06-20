import sys,tkinter,os,cv2,pygame,random,pdb,csv
from tkinter import filedialog

def config(event):

	def end_e():
		with open("./src/conf.txt","w") as f:
			f.write(txt_conf.get())
			d_conf.destroy()
   	
	d_conf=tkinter.Tk()
	d_conf.geometry("400x300")
	d_conf.title("設定")

	with open("./src/conf.txt","r") as f:
		buf_size_config=f.read()
  
  	# ラベル
	lbl_conf = tkinter.Label(d_conf,text='ずらせる画像幅：')
	lbl_conf.place(x=10, y=50)
	# テキストボックス
	txt_conf = tkinter.Entry(d_conf,width=15)
	txt_conf.insert(tkinter.END,buf_size_config)
	txt_conf.place(x=50, y=70)
  
	#box
	b_end=tkinter.Button(d_conf,text="完了",command=end_e)
	b_end.place(x=180,y=240)

	d_conf.mainloop()