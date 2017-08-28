from datetime import datetime
time_stamp=str(datetime.now())[:19]
time_stamp2=time_stamp[:13]+'-'+time_stamp[14:16]+'-'+time_stamp[17:19]
print(time_stamp)
print(time_stamp2)

tcs=open(time_stamp2+".txt","a")

tcs.write("Anu")
