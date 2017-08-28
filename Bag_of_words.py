import math


def bag_of_words(file1,file2):
	list1=[]
	dict_file1={}
	dict_file2={}
	for line in file1:
		list1.extend(line.split(" "))

	for word in list1:
		if word in dict_file1:
			dict_file1[word]+=1
		else:
			word=word.strip("\n")
			word_list=list(word)
			for i in word_list:
				
				if not (ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122 or ord(i)>=48 and ord(i)<=57 and i=="_"):
					word_list.remove(i)
					
			word1=''.join(word_list)
			dict_file1.update({word1.lower():1})
	
	list1=[]
	for line in file2:
		list1.extend(line.split(" "))

	for word in list1:
		if word in dict_file2:
			dict_file2[word]+=1
		else:
			word=word.strip("\n")
			word_list=list(word)
			for i in word_list:
				
				if not (ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122 or ord(i)>=48 and ord(i)<=57 and i=="_"):
					word_list.remove(i)
					
			word1=''.join(word_list)
			dict_file2.update({word1.lower():1})
	
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
	cos = round(cos*100)
	return cos

file1=open("trial.txt")
file2=open("trial2.txt")
bag_of_words(file2,file1)
file1.close()
file2.close()