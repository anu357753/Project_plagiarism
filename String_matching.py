def string_matching(file1,file2):
	lcs=0
	list1=[]
	for line in file1:
		list1.extend(line.split())
	list2=[]
	for line in file2:
		list2.extend(line.split())
	list3=[]
	i,j=0,0
	count=0
	while(i<len(list1)):
		
		if lcs<count:
			lcs=count
		if len(list3)!=0:
			print(list3)
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
	
	len1=0
	for i in list1:
		len1+=len(i)
	for i in list2:
		len1+=len(i)

	lcs_f = ((lcs * 2)/(len1))*100

	return lcs_f

file1=open("trial5.txt")
file2=open("trial.txt")
string_matching(file1,file2)