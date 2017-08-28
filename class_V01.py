from os import listdir
import os, glob
import math
from datetime import datetime
from stop_words import stop_words

class Plagiarism(object):
	"""docstring for Plagiarism"""
	def __init__(self,files):
		self.files=files

	def fileread(self,file):
		''' This function takes a file as input,
			opens the file and 
			returns the file'''


		open_file=open(file)
		return open_file


	def word_dict_list(self,file):
		
		''' This function takes a file as input,
				It separates all the words in the file, removing spaces and special characters.
				It takes the frequencies of each word in the file into a dictionary.
				The dictionary has key as each word and value as the frequency of its occurence.
				It forms a list of all the words in the document.
				It returns the dictionary and the list. '''


		list1=[]
		dict_file1={}
		list_file1=[]

		for line in file:
			list1.extend(line.split(" "))
		if len(list1)!=0:
			
			for word in list1:
				if word in dict_file1:
					dict_file1[word]+=1
					list_file1.append(word)
				else:
					word=word.strip("\n")
					word_list=list(word)
					word_list2=[]
					for i in word_list:
						
						if (ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122 or ord(i)>=48 and ord(i)<=57 and i=="_"):
							word_list2.append(i)
							
					word1=''.join(word_list2)
					if word1!='':
						list_file1.append(word1)
						dict_file1.update({word1.lower():1})
			return (dict_file1,list_file1)
		else:
			return None

	def create_dict_list(self,log_file):

		''' This function checks if a file is empty and alerts the user.
		        If the file is not empty,
		            it appends all the dictionaries and lists returned from another function
		            into two separate lists.

		            It returns the two lists and a list of files that are not empty   '''
		


		dict_list=[]
		list_list=[]
		files2=[]
		for file in self.files:
			read=self.fileread(file)
			dict_list_tup=self.word_dict_list(read)
			if dict_list_tup==None:
				print("\n")
				print(file, " is empty. It will not be tested for plagiarism.")
				log_file.write(file+ " is empty. It will not be tested for plagiarism.")
				log_file.write("\n")
			else:
				dict_list.append(dict_list_tup[0])
				list_list.append(dict_list_tup[1])
				files2.append(file)
		return (dict_list,list_list,files2)

	def bag_of_words(self,dict_file1,dict_file2):

		''' This function takes two dictionaries of frequency of words for two files,
								and returns the similarity between the two files in terms of words '''
		
		dot_prod=0
		for i in dict_file1:
			if i in dict_file2:
				dot_prod+=(dict_file2[i]*dict_file1[i])
				
		list1=list(dict_file1.values())
		squares1=0
		for i in list1:
			squares1+=(i**2)
		
		list1=list(dict_file2.values())
		squares2=0
		for i in list1:
			squares2+=(i**2)

		cos=dot_prod/(math.sqrt(squares2)*math.sqrt(squares1))
		cos = (cos*100)
		return cos

	def string_matching(self,list1,list2):

		'''  This function takes two lists and 
		           				returns the percentage occupied by the longest common string in each file '''
		
		if len(list1)<len(list2):
			list1,list2=list2,list1
		lcs=0
		i,j=0,0
		count,flag=0,0
		len1=0
		

		while (i<len(list1)):
			if lcs<count:
				lcs=count
			count=0
			j=0
			while (j<len(list2) and i<len(list1)):
				
				flag=0
				if list1[i].lower() == list2[j].lower():
					count+=len(list2[j])
					i+=1
					j+=1
				else:
					if lcs<count:
						lcs=count
					count=0
					j=0

					while(j<len(list2) and i<len(list1) and list1[i].lower()!=list2[j].lower()):
						j+=1
						if j==len(list2):
							flag=1
			if flag==1:





				i+=1

		if lcs<count:
			lcs=count
		for i in list1:
			len1+=len(i)
		for i in list2:
			len1+=len(i)
		
		lcs_f = ((lcs * 2)/(len1))*100
		return lcs_f

	def filter_string(self,file):
		stop_word=stop_words()
		list1=[]
		finger_string=""

		for line in file:
			list1.extend(line.split(" "))
		if len(list1)!=0:
			
			for word in list1:
				if word not in stop_word:
					word=word.strip("\n")
					word_list=list(word)
					word_list2=[]
					for i in word_list:
						
						if (ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122 or ord(i)>=48 and ord(i)<=57 and i=="_"):
							word_list2.append(i)
							
					word1=''.join(word_list2)
					finger_string+=word1.lower()
			return (finger_string)
		else:
			return None

	def create_string_list(self):
		string_list5=[]
		for file in files:
			read=self.fileread(file)
			fin_string=self.filter_string(read)
			string_list5.append(fin_string)	
		
		return (string_list5)

	def make_hashes(self,string1):
		word_list=[]
		hash_list=[]

			
		for i in range(len(string1)-5):
			word_list.append(string1[i:i+5])
		
		for word in word_list:
			hash_num=0
			for let in range(len(word)):
				hash_num+=(ord(word[let])*(5**((len(word))-let)))
				hash_num2=hash_num%10007
			hash_list.append(hash_num2)

		return hash_list

	def hash_key(self):
		main_list=[]
		list_string=self.create_string_list()
		for string in list_string:
			if string!=None:
				main_list.append(self.make_hashes(string))
		return main_list

	def finger_printing(self,list_hash1,list_hash2):
	
		count=0
		for i in list_hash1:
			for j in list_hash2:
				if i==j:
					count+=1
		percent=((count*2)/(len(list_hash1)+len(list_hash2)))*100
		return percent


path=input("Enter the directory: ")
os.chdir(path)
files=[p for p in listdir(path) if p.endswith('.txt') and p!='log_file.txt']
p=Plagiarism(files)

class Driver(object):
	
	
	def main(self):

		'''    This is the main function, it uses all the functions mentioned above to check for plagiarism 
					for given files.		   '''

		log_file=open("log_file.txt","a")
		log_file.write("\n")
		time_stamp=str(datetime.now())[:19]
		log_file.write("    "+time_stamp+"    ")
		log_file.write("\n")
		log_file.write("    -------------------")
		log_file.write("\n")
		dict_list_tup=p.create_dict_list(log_file)
		dict_list=dict_list_tup[0]
		list_list=dict_list_tup[1]
		files_2=dict_list_tup[2]
		hash_list=p.hash_key()
		
		
		print("\n")
		print("           Plagiarism Test   ")
		print("           ---------------")
		log_file.write("\n")

		if len(dict_list)==0:
			print(" There are no files in the directory")
			log_file.write(" There are no files in the directory")
		elif len(dict_list)==1:
			print("There is only one file in the directory")
			log_file.write("There is only one file in the directory")
		
		else:
			for i in range(len(dict_list)):
				
				for j in range(i,len(dict_list)):

					if i!=j:
						try:
							log_file.write("\n")
							print("Plagiarism for files ", files_2[i]," ",files_2[j],":")
							log_file.write("Plagiarism for files "+files_2[i]+" "+files_2[j]+":")
							log_file.write("\n")

							cos=p.bag_of_words(dict_list[i],dict_list[j])
							print("Bag of words:    ",cos)
							log_file.write("Bag of words:    "+str(cos))
							log_file.write("\n")

							lcs=p.string_matching(list_list[i],list_list[j])
							print("String Matching: ",lcs)
							log_file.write("String Matching: "+str(lcs))
							log_file.write("\n")

							percent=p.finger_printing(hash_list[i],hash_list[j])
							print("Finger Printing: ",percent)
							print("\n")
							log_file.write("Finger Printing: "+str(percent))
							log_file.write("\n")
						except ZeroDivisionError:
							print("One or both the files have invalid input")
							print("\n")
							log_file.write("One or both the files have invalid input")
							log_file.write("\n")
			log_file.write("************************************************************")

d=Driver()
d.main()