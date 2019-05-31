import os
import random
import string

# list all directory file and the subdirectory files
def show_dir(filepath):
    for i in os.listdir(filepath):
        path = os.path.join(filepath,i)
        print(path)
        if os.path.isdir(path):
            show_dir(path)

#show_dir(os.curdir)

# find html file in current directory and all subdirectory.
def find_html(filepath):
    for i in os.listdir(filepath):
        path = os.path.join(filepath,i)
        if os.path.isdir(path):
            find_html(path)
        if path.endswith('html'):
            print(path)
            
#find_html(os.curdir)

def wordsReplace(oldWord, newWord):
	pf_file = os.listdir()
	
	for i, name in enumerate(pf_file):
		if name.startswith('_') or not name.endswith('.py'):
			pf_file.remove(name)
	
	for file in pf_file:
		with open(file,'a+') as f:
			f.seek(0)
			all_text = f.readlines()
			for i, s in enumerate(all_text):
				all_text[i] = s.replace(oldWord, newWord)
			f.seek(0)
			f.writelines(all_text)
			
#wordsReplace('@loginrequired()','@loginrequired')

# swap key and value in dictionary
dict1 = {"A":1,"B":2,"C":3}
dict2 = {y:x for (x,y) in dict1.items()}
print(dict2)

#generate random n chars
def ranChars(nchars):
    L = []
    for ascii in [range(65,91),range(97,123),range(48,58)]:
        for char in ascii:
            L.append(chr(char))
    return random.sample(L,nchars)

#print(''.join(ranChars(6)))

def ranChars2(nchars):
    s = string.digits + string.ascii_letters
    return random.sample(s, nchars)

#print(''.join(ranChars2(10)))


print('square root: %0.6f' % 2**0.5)