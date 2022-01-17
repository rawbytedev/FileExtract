import urllib.request
import os
import time
logo = """

             |
             |        - FileExtract -
             | Author: Xnetwolf(Radiationbolt)
             | 
             | Extract chosen files from github
"""
print(logo)

sysroot = os.path.expanduser("~")
try:
	open("logs.txt", "r")
except:
	option = "1"
	open("logs.txt", "w").write("Xnetwolf(radiationbolt)")
else:
	option = "0"
	
if option == "1":
	print("Welcome to FileExtract by Xnetwolf")
	print()
	time.sleep(0.8)
	print("""I will guide you because it's your first time using this tool
	Thanks for downloading FileExtract""")
	time.sleep(1)
	print("getting everything ready")
	os.system("clear")
	print(logo)
username = input("username: ")
repo_name = input("repo name: ")
PathToFile = input("path to file in github: ")
save = input("Where to save download: ")
extract = f'https://raw.githubusercontent.com/{username}/{repo_name}/{PathToFile}' #use raw.githubusercontent.com
print(f"extracting {PathToFile} from https://github.com/{username}/{repo_name} ")

urllib.request.urlretrieve(extract, save)

print(f"saved in {save}")
