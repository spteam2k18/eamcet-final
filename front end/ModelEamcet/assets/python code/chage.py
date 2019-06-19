import os
for filename in os.listdir("6"):
    #print(filename)
    a = filename.find(".")
    b = filename[0:a] + ".JPG"
    os.rename("6/"+filename,"6/"+b)
