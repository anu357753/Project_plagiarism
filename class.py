from os import listdir
import os, glob
import math
from datetime import datetime

class  Plagiarism(object):
	"""docstring for  Plagiarism"""
	def __init__(self, file_list):
		self.file_list=file_list

	def Open(self,file):
		open_file=open(file)
		return open_file	

	def make_dict(self):

		for file in self.file_list:	
			print(file)
			open_file=self.Open(file)
			for line in open_file:
				print(line)



path=input("Enter the directory: ")
os.chdir(path)
files=[p for p in listdir(path) if p.endswith('.txt') and p!='log_file.txt']

object1=Plagiarism(files)
object1.make_dict()