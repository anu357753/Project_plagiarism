from os import listdir
import math

path=input("Enter the directory: ")

files=[p for p in listdir(path) if p.endswith('.txt')]


def fileread(file):
	open_file=open(file)
	return open_file

def word_dict_list(file):
	
	list1=[]
	dict_file1={}
	list_file1=[]
	for line in file:
		list1.extend(line.split(" "))

	for word in list1:
		if word in dict_file1:
			dict_file1[word]+=1
			list_file1.append(word)
		else:
			word=word.strip("\n")
			word_list=list(word)
			for i in word_list:
				
				if not (ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122 or ord(i)>=48 and ord(i)<=57 and i=="_"):
					word_list.remove(i)
					
			word1=''.join(word_list)
			list_file1.append(word1)
			dict_file1.update({word1.lower():1})

	return (dict_file1,list_file1)

def create_dict_list():
	dict_list=[]
	list_list=[]
	for file in files:
		read=fileread(file)
		dict_list_tup=word_dict_list(read)
		dict_list.append(dict_list_tup[0])
		list_list.append(dict_list_tup[1])
	return (dict_list,list_list)

def bag_of_words(dict_file1,dict_file2):
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
	# cos = round(cos*100)
	return cos

def string_matching(list1,list2):
	lcs=0
	i,j=0,0
	count=0
	len1=0
	while(i<len(list1)):
		
		if lcs<count:
			lcs=count
		count=0
		j=0
		
		while(j<len(list2) and i<len(list1)):
			if list1[i]==list2[j]:
				count+=len(list2[j])
				i+=1
				j+=1
			else:
				if lcs<count:
					lcs=count
				count=0
				j+=1
		i+=1
		
	if lcs<count:
		lcs=count
	
	
	for i in list1:
		len1+=len(i)
	for i in list2:
		len1+=len(i)

	lcs_f = ((lcs * 2)/(len1))

	return lcs_f

def main():
	dict_list_tup=create_dict_list()
	dict_list=dict_list_tup[0]
	list_list=dict_list_tup[1]
	for i in range(len(dict_list)):
		
		for j in range(i,len(dict_list)):

			if i!=j:
				try:
					print("Plagiarism for files ", files[i]," ",files[j],":")
					cos=bag_of_words(dict_list[i],dict_list[j])
					print("Bag of words: ",cos)
					lcs=string_matching(list_list[i],list_list[j])
					print("String Matching: ",lcs)
					print("\n")
				except ZeroDivisionError:
					print("One of the files is empty")
					print("\n")
				except:
					print("Some error occured")
			

main()
