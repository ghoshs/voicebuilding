import os
import sys

def extract(filename, flacname):
	fp = open(filename).read()
	auddirectory = os.getcwd()+'/audio'
	textdirectory = os.getcwd()+'/text'
	if not os.path.exists(textdirectory):
	    os.makedirs(textdirectory)
	if not os.path.exists(auddirectory):
	    os.makedirs(auddirectory)

	for line in fp.split('\n'):
		if (len(line.split('\t'))<3):
			continue
		id = line.split('\t')[0]
		text = line.split('\t')[1]
		startt = line.split('\t')[2]
		endt = line.split('\t')[3]
		command = "sox channel1.wav audio/"+id+".wav trim "+startt+"  ="+endt
		os.system(command)
		fp1 = open('text/'+id+'.txt', 'w')
		fp1.write(text)
		fp1.close()

def main():
	if (len(sys.argv[1:]) == 2):
		extract(sys.argv[1], sys.argv[2])
	else:
		print("Not enough arguments!")
	# extract("extractinfo.txt", "channel1.wav")

if __name__ == "__main__":
	main()