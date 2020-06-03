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
	print("reader",(reader))
	read=(csv.reader(reader))
	print("read",read)
	l=[row for row in read]

	print("l: ",l,type(l))
		
	pos=0#初期化
	if not(score=="-1"):#-1:ランキング表示時。-1以外:スコア書き込み
		for cnt in l:
			if int(l[pos][1])<int(score):
				break
			pos+=1

		add=[0]*2
		add[0]=name
		add[1]=score
		adder=[add]
		l.insert(pos-1,add)
		# in_put=",".join(l[0:9])
		# in_put.encode()

		with io.StringIO() as f:
			sys.stdout=f
			print(l)
			in_put=f.getvalue()
			sys.stdout=sys.__stdout__
			in_put=in_put.rstrip("\n")
			print(in_put,",",type(in_put))

		crypt_csv(in_put)

	return l

#testbench#
fileoc(sys.argv[1],sys.argv[2])