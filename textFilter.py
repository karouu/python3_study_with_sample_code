import os

pf_file = os.listdir()

for i,name in enumerate(pf_file):
	if name.startswith('_') or not name.endswith('.py'):
		pf_file.remove(name)


for file in pf_file:
	with open(file,'a+') as f:
		all_text = f.readlines()
		for i, s in enumerate(all_text):
			all_text[i] = s.replace('@loginrequired()','@loginrequired')
		f.seek(0)
		f.writelines(all_text)