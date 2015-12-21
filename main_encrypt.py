#codec v1.0

#insert user key 'foobar'
key = raw_input("Enter key: ")
key = list(str(hash(key)))
# A 0 in the key hash will invalidate the encryption...quick fix for now.
if '0' in key:
	print "Invalid"
	exit()

encrypt=[]	
for i in key:
    try:
    	encrypt.append(int(i))
    except ValueError:
        pass


# raw data prep into list        
r_data = open('file.txt', 'r').read()             
data = list(r_data)

# ENCRYPTION
# v1.0 
mod = encrypt[:]
for i in xrange(len(data)-1):
    if len(mod) >= 1:
    	data[i] = ord(data[i])*mod.pop(0)
    else: 
    	mod = encrypt[:]
    	data[i] = ord(data[i])*mod.pop(0)
		
# Write encrypted data to file
with open('e_data.txt', 'wb') as f:  
    for i in data:
    	f.write(str(i)+'\t') 
                                                                                                                                                                                                                                                                                                                                                       
