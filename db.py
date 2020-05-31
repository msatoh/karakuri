#coding: UTF-8
import sys,csv,pdb,cryptography
from cryptography.fernet import Fernet

key=b"23456789012345678901234azZa+216549780219021="

def crypt_csv():
	with open("src/rank.csv","rb") as f:
		data=f.read()
		fernet=Fernet(key)
		encrypted=fernet.encrypt(data)
	with open("src/rank.csv","wb") as f:
		f.write(encrypted)

def dec_csv():
	with open("src/rank.csv","rb") as f:
		data=f.read()
		if data==b"":
			return -1
		fernet=Fernet(key)
		decrypted=fernet.decrypt(data)		
	with open("src/rank.csv","wb") as f:
		f.write(decrypted)
	return 0

def fileoc(name,score):
	dec_csv()
	with open("src/rank.csv") as f:
		reader=csv.reader(f)
		# for row in reader:
		# 	print("row: ",row)
		l=[row for row in reader]
		print("l: ",l)
		
		pos=0#初期化
		if not(score=="-1"):
			for cnt in l:
				if int(l[pos][1])<int(score):
					break
				pos+=1

	if not(score=="-1"):	#-1:ゲーム終了時、スコア書き込み
		with open("src/rank.csv",mode="w") as f:
			writer=csv.writer(f)
			add=[0]*2
			add[0]=name
			add[1]=score
			adder=[add]
			l.insert(pos-1,add)
			writer.writerows(l[0:9])
			#f.writelines(add)
	crypt_csv()

	return l

#testbench#
fileoc(sys.argv[1],sys.argv[2])