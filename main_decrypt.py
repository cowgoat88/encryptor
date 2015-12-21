# DE-codec v1.0

#insert user key dev='foobar'
key = raw_input("Enter key: ")

# Initialize DEcryption 
# Use hash of password into list 
# Will use ints from hash to mod chars in data
key = list(str(hash(key)))
decrypt=[]
for i in key:
    try:
        decrypt.append(int(i))
    except ValueError:
        pass
        
# Prep encrypted file into list        
with open('e_data.txt', 'rb') as f:
	e_data = f.read()
	
data = e_data.split('\t')

# Cleans up data
while True:
	try:
		data.remove('\n')
		data.remove('')
	except ValueError:
		break

# DECRYPTION
# v1.0 

mod = decrypt[:] 
try:
	for i in xrange(len(data)):
		if len(mod) >= 1:
			data[i] = chr(int(data[i])/mod.pop(0))
		else: 
			mod = decrypt[:]
			data[i] = chr(int(data[i])/mod.pop(0))
	print "Decrypted data:\n",''.join(data)
except:
	print "DECRYPTION FAILED\n\n\n"
		

