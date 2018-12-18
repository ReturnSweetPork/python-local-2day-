import os

os.chdir(r'C:\Users\student\hyunsang\SSAFY지원자')


for filename in os.listdir("."):

    after_name = print(filename.replace("SAMSUMG_SAMSUMG","SSAFY"))


    os.rename(filename, after_name)









