import hashlib

secret_key = 'iwrupvqb'
for i in range(100000000):
    out = hashlib.md5(secret_key + str(i)).hexdigest()
    if out.startswith('000000'):
        print i
        break
