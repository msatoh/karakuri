import sys,csv,pdb,cryptography
from cryptography.fernet import Fernet

key=b"23456789012345678901234azZa+216549780219021="

def crypt_csv():
	with open("src/rank.csv","rb") as f:
		data=f.read()
		fernet=Fernet(key)
		encrypted=fernet.encrypt(data)
	with open("src/rank_enc.csv","wb") as f:
		f.write(encrypted)

def dec_csv():
	with open("src/rank_enc.csv","rb") as f:
		data=f.read()
		fernet=Fernet(key)
		decrypted=fernet.decrypt(data)
	with open("src/rank_dec.csv","wb") as f:
		f.write(decrypted)

def fileoc(name,score):
	with open("src/rank.csv") as f:
		reader=csv.reader(f)
		# for row in reader:
		# 	print("row: ",row)
		l=[row for row in reader]
		print("l: ",l)
		# l=list(itertools.chain.from_iterable(l))
		# print("chain_l: ",l)
		# ll=[l]
		# print("ll: ",ll)
	with open("src/rank.csv",mode="w") as f:
		writer=csv.writer(f)
		if(name=="0"):
			writer.writerow("")
		else:
			add=[0]*2
			add[0]=name
			add[1]=score
			adder=[add]
			print("adder: ",adder)
			l.append(add)
			print("l2: ",l)
			writer.writerows(l)
			#f.writelines(add)

#testbench#
fileoc(sys.argv[1],sys.argv[2])
crypt_csv()
dec_csv()