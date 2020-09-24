from Crypto.Cipher import AES
import random
import pass_gen
import Padding

# key='1234567891234567'
# iv = ''.join([chr(random.randint(0, 100)) for i in range(16)])
# obj = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
# data = "hello" # <- 16 bytes
# data=Padding.appendPadding(data, blocksize=16, mode='CMS')
# encd = obj.encrypt(data.encode("utf8"))
# print(encd)
# obj1=AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
# decr=obj1.decrypt(encd)
# decr=Padding.removePadding(decr.decode(), blocksize=16, mode='CMS')
# print(decr)

def encoder(data,key,iv):

	obj = AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
	data=Padding.appendPadding(data, blocksize=16, mode='CMS')
	encd = obj.encrypt(data.encode("utf8"))
	return encd

def decoder(data,key,iv):

	obj1=AES.new(key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
	decr=obj1.decrypt(data)
	decr=Padding.removePadding(decr.decode(), blocksize=16, mode='CMS')
	return decr