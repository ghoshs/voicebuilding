import sys
import os

def process(tablefile, promptsfile):
	
	table = open(tablefile).read()
	prompts = open(promptsfile).read()
	tabledata = table.split('\n')[1:-1]
	# print(len(timedata))
	promptdata = prompts.split('\n')[0:330]
	# print(len(promptdata))
	length = len(promptdata)

	# create a yaml file
	fp = open('build/metaData.txt','w')

	# copy text in separate file
	for i in range(0, length):
		promptLine = promptdata[i].split('"')
		id = promptLine[0].split(' ')[1]
		text = promptLine[1]

		tableLine = tabledata[i].split('\t')
		fp.write(id+'\t'+text+'\t'+tableLine[0]+'\t'+tableLine[2]+'\n')
	fp.close()

def main():
	if (len(sys.argv[1:]) == 2):
		process(sys.argv[1], sys.argv[2])
	else:
		print("Not enough arguments!")
	# process('Annotations.Table', 'cmuarctic.data.txt')

if __name__ == "__main__":
	main()