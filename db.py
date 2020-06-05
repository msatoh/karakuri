#coding: UTF-8
import sys,io,csv,pdb,cryptography
from cryptography.fernet import Fernet

key=b"23456789012345678901234azZa+216549780219021="

def crypt_csv(list):
	data=list.encode()
	fernet=Fernet(key)
	encrypted=fernet.encrypt(data)
	with open("src/rank.csv","wb") as f:
		f.write(encrypted)

def dec_csv():
	with open("src/rank.csv","rb") as f:
		data=f.read()
		if data==b"":
			return data
		fernet=Fernet(key)
		return fernet.decrypt(data)

def fileoc(name,score):
	reader=dec_csv()
	reader=reader.decode()
	#print("reader",reader)
	if not(reader==""):
		#print("initial")
		l=reader.split("\n")
		pos=0
		for cnt in l:
			l[pos]=l[pos].split(",")
			pos+=1
	else:
	 	l=[]

	#print("l: ",l,type(l))
	pos=0#初期化

	if not(score=="-1"):#-1:ランキング表示時。-1以外:スコア書き込み
		if not(l==[]):
			for cnt in l:
				if int(l[pos][1])<int(score):
					break
				pos+=1

		l.insert(pos,[name,score])
		l=l[0:9]
		#print("l",l)

		with io.StringIO() as f: #l→crypt_csvに文字列として渡す
			sys.stdout=f
			writer=csv.writer(f,lineterminator="\n")
			writer.writerows(l)
			in_put=f.getvalue()
			sys.stdout=sys.__stdout__
			in_put=in_put.rstrip("\n")
			#print(in_put,"&",type(in_put))

		crypt_csv(in_put)

	return l

#testbench#
#fileoc(sys.argv[1],sys.argv[2])