import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    install('python-dotenv')
    print("python-dotenv installed.")
except:
    print("python-dotenv failed to install.")

try:
    install('pandas')
    print("pandas installed.")
except:
    print("pandas failed to install.")

try:
    install('discord')
    print("discord installed.")
except:
    print("discord failed to install.")

try:
    writeProc = open("maindb.csv", "w")
    writeProc.write("ID,Name,Value\n")
    writeProc.write("0,Total triggers,0\n")
    writeProc.write("1,Channel triggers,0\n")
    writeProc.write("2,Video triggers,0\n")
    print("Created database successfully.")
    writeProc.close()

except:
    print("Failed to create database.")

print("Insert your Discord bot token:")
token = input()

try:
    writeProc = open(".env", "w")
    writeProc.write("TOKEN=" + token)
    print("Token file created")
    writeProc.close()

except:
    print("Failed to create token file.")

print ("You may now run this command:")
print ("python3 main.py")