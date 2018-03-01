import os
import sys

def extract(filename, flacname):
	fp = open(filename).read()
	audpath = 'build/wav'
	textpath = 'build/text'
	auddirectory = os.getcwd()+'/'+audpath
	textdirectory = os.getcwd()+'/'+textpath
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
		command = "sox 2018-voicebuilding-group1-raw-audio.flac -r 16k "+audpath+"/"+id+".wav trim "+startt+"  ="+endt+" remix 1"
		os.system(command)
		fp1 = open(textpath+'/'+id+'.txt', 'w')
		fp1.write(text)
		fp1.close()

def main():
	if (len(sys.argv[1:]) == 2):
		extract(sys.argv[1], sys.argv[2])
	else:
		print("Not enough arguments!")
	# extract("metaData.txt", "channel1.wav")

if __name__ == "__main__":
	main()