import os
for filename in os.listdir("1"):
    #print(filename)
    a = filename.find(".")
    b = filename[0:a] + ".JPG"
    os.rename("1/"+filename,"1/"+b)
