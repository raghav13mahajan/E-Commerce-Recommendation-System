f=open("oo.txt",'r')
f2 = open("new_oo.json",'w')
for line in f:
    s = line.split()
    #print line
    new_line = ' '.join(s[i] for i in range(len(s)))
    new_line += "," 
    new_line += "\n"
    #print new_line
    f2.write(new_line)
f.close()
f2.close()

    
    
