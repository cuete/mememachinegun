#!/usr/bin/env python
#Just another meme machine gun

import random
import os

__author__ = "el cuete"
__copyright__ = "Copyright (C) 2018 el cuete"
__license__ = "MIT"
__version__ = "0.1"

text = ['o rly?', 'ya rly', 'no, rly', 'etc'] #assorted phrases

def main():
	source = 'pic.jpg' #source pic
	output = 'meme.jpg' #destination file name for meme
	generateMeme(source, output)
	
def generateMeme(source, output):
	sub = randomPhrase()
	#add random phrase to image
	os.system("convert {} -gravity south -stroke '#000' -strokewidth 1 -fill white -font Impact -pointsize 72 -annotate 0 '{}' {}".format(source,sub,output))

def randomPhrase():
	#select random phrase
	randomInt = random.randint(0,len(text))
	return text[randomInt].upper()

if __name__ == "__main__":
    main()
