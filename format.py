name="264"
a=open("%s.txt"%(name),"r")
txt=a.read().split("\n")
output=[]
for i,ele in enumerate(txt):
	if ".pdf" in ele:
		output.append(ele.split("&")[0])
b=open("%s_o.txt"%(name),"w")
for ele in output:
	b.write(ele+"\n")
b.close()

