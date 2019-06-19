import os
for filename in os.listdir("4"):
    #print(filename)
    a = filename.find(".")
    b = filename[0:a] + ".JPG"
    os.rename("4/"+filename,"4/"+b)
