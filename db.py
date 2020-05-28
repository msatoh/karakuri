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
		fernet=Fernet(key)
		decrypted=fernet.decrypt(data)
	with open("src/rank.csv","wb") as f:
		f.write(decrypted)

def fileoc(name,score):
	dec_csv()
	with open("src/rank.csv") as f:
		reader=csv.reader(f)
		# for row in reader:
		# 	print("row: ",row)
		l=[row for row in reader]
		# l=list(itertools.chain.from_iterable(l))
		print("l: ",l)
		# ll=[l]
		# print("ll: ",ll)

	if not(score=="-1"):
		with open("src/rank.csv",mode="w") as f:
			writer=csv.writer(f)
			add=[0]*2
			add[0]=name
			add[1]=score
			adder=[add]
			l.append(add)
			writer.writerows(l)
			#f.writelines(add)
	crypt_csv()

	return l

#testbench#
#fileoc(sys.argv[1],sys.argv[2])