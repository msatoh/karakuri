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
		data.decode()
		if data==b"":
			return data
		fernet=Fernet(key)
		return fernet.decrypt(data)

def fileoc(name,score):
	reader=dec_csv()
	reader.decode()
	# for row in reader:
	# 	print("row: ",row)
	l=[row for row in reader]
	print("l: ",l)
		
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
			in_put.encode()
			sys.stdout=sys.__stdout__
		# i=0
		# j=0
		# for rnk in l:
		# 	for elm in rnk:
		# 		in_put[i][j]=elm.encode()
		# 		j+=1
		# 	i+=1
		crypt_csv(in_put)

	return l

#testbench#
fileoc(sys.argv[1],sys.argv[2])