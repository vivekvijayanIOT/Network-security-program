import pyDes
data = "Please encrypt my data"
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)

print "Encrypted: %r" % d





import hashlib
s=hashlib.sha1("abc").hexdigest();
print s

import hashlib
s=hashlib.md5("abc").hexdigest();
print s
