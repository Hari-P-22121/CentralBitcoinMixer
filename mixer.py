import bitcoin
import sys
from bit import Key
import binascii
import hashlib
import base58
import os
import random

hm = os.getenv("HOME")


f = open(hm+'/mixJob.txt', 'r')
ff = f.readlines()
f.close()

finalDrop = []

# priv_key_Center = bitcoin.random_key()
# addressCenter = bitcoin.privkey_to_address(priv_key)

# for m in range(len(ff)):

# 	dat = ff[m]

# 	priv_key = dat.split(':')[1]

# 	extended_key = "80"+priv_key

# 	first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()

# 	second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()

# 	final_key = extended_key+second_sha256[:8]

# 	WIF = base58.b58encode(binascii.unhexlify(final_key))

# 	WIF = WIF.decode("utf-8")

# 	kk = Key(WIF)

# 	bal = kk.get_balance('satoshi')
# 	bal = bal-150

# 	ff[m] = ff[m]+':'+bal

# 	finalDrop += dat.split(':')[0]+':'+bal

# 	outputs = [addressCenter, bal, 'satoshi']

# 	totalBal += bal

# 	kk.send(outputs, fee=50)


# eachAmnt = (totalBal-50)/len(ff)
# eachAmnt = (int)eachAmnt

# outputs2 = []

# privs = []

# for dat in ff:
# 	priv_key = dat.split(':')[1]
# 	privs.append(priv_key)
# 	outputs2.append(bitcoin.privkey_to_address(priv_key), eachAmnt, 'satoshi')



# extended_key = "80"+priv_key_Center

# first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()

# second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()

# final_key = extended_key+second_sha256[:8]

# WIF = base58.b58encode(binascii.unhexlify(final_key))

# WIF = WIF.decode("utf-8")

# kk = Key(WIF)

# kk.send(outputs2, fee=50)

# random.shuffle(privs)

# eachAmnt = eachAmnt-50

# pI = 0



# for i in range(len(privs)):
# 	privKey = privs[i]
# 	recp = ff[pI].split(':')[0]
# 	amnt = (int)ff[pI].split(':')[2]

# 	extended_key = "80"+priv_key_Center

# 	first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()

# 	second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()

# 	final_key = extended_key+second_sha256[:8]

# 	WIF = base58.b58encode(binascii.unhexlify(final_key))

# 	WIF = WIF.decode("utf-8")

# 	kk = Key(WIF)

# 	bal = kk.get_balance('satoshi')

# 	bal = bal-50

# 	outputs = [recp, amnt, 'satoshi']

# 	kk.send(outputs, fee=50)

# 	partA = ff[pI].split(':')[0]
# 	partB = ff[pI].split(':')[1]
# 	partC = (int)ff[pI].split(':')[2]
# 	partC = partC-amnt

# 	ff[pI] = partA+':'+partB+':'+partC

# 	if(bal >= amnt):
# 		pI += 1

for m in range(len(ff)):

	dat = ff[m]

	priv_key = dat.split(':')[1]

	extended_key = "80"+priv_key

	first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()

	second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()

	final_key = extended_key+second_sha256[:8]

	WIF = base58.b58encode(binascii.unhexlify(final_key))

	WIF = WIF.decode("utf-8")

	kk = Key(WIF)

	bal = kk.get_balance('satoshi')
	bal = bal-50

	ff[m] = ff[m]+':'+bal

def split_big_num(num):
    partition = randint(3,5)
    piece = randint(1,int(num))
    result = []
    for i in range(partition):
        element = num-piece
        result.append(element)
        piece = randint(0,element)
        if num - piece == 0:
            return result
    return result


for i in range(len(ff)):

	dat = ff[i]

	matchAddr = dat.split(':')[0]

	priv_key = dat.split(':')[1]

	remainBalance = dat.split(':')[2]

	srcAddr = bitcoin.privkey_to_address(priv_key)

	extended_key = "80"+priv_key

	first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()

	second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()

	final_key = extended_key+second_sha256[:8]

	WIF = base58.b58encode(binascii.unhexlify(final_key))

	WIF = WIF.decode("utf-8")

	kk = Key(WIF)

	totalBal = kk.get_balance("satoshi")

	totalBal = totalBal - 50

	sends = split_big_num(totalBal)

	outputs = []

	while sum(sends) > 0:

		randChoice = random.randint(0, len(ff))

		while((i == randChoice) and (ff[randChoice].split(':')[2] <= 0)):
			randChoice = random.randint(0, len(ff))

		tmpSend = ff[randChoice]

		tmpAddr = tmpSend.split(':')[0]
		tmpVal = tmpSend.split(':')[2]
		
		sending = random.choice(sends)
		while sending <= 0:
			sending = random.choice(sends)

		vall = sending
		if(sending > tmpVal):
			vall = tmpVal
		else:
			vall = sending

		remainBalance = remainBalance - vall

		dat = dat.split(':')

		dat[2] = remainBalance

		dat = dat[0]+':'+dat[1]+':'+dat[2]

		ff[i] = dat

		finalBal = tmpVal - vall

		parts = ff[randChoice].split(':')

		parts[2] = finalBal

		ff[randChoice] = parts[0]+':'+parts[1]+':'+parts[2]

		outputs.append(tmpAddr, vall, 'satoshi')

	#kk.send(outputs, fee=50)












