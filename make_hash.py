from stop_words import stop_words
def filter_string(file):
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

def create_string_list():
	string_list5=[]
	for file in files:
		read=fileread(file)
		fin_string=filter_string(read)
		string_list5.append(fin_string)	
	return (string_list5)

def make_hashes(string1):
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

def hash_key():
	main_list=[]
	list_string=create_string_list()
	for string in list_string:
		main_list.append(make_hashes(string))
	return main_list


def finger_printing(list_hash1,list_hash2):
	count=0
	for i in list_hash1:
		for j in list_hash2:
			if i==j:
				count+=1
	percent=((count*2)/(len(list_hash1)+len(list_hash2)))*100
	return percent
