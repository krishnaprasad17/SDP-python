#APPEND AND DISPLAY
appendme="\n added this line into file"
appendfile=open("test.txt", "a") 
appendfile.write(appendme)
appendfile.close()
