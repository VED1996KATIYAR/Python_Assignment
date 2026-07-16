


try:
    file=open("sample.txt",'rt')
    file.seek(0)
    line1=file.readline()
    line2=file.readline()
    file.close()
    print(f"Line 1 :{line1}")
    print(f"Line 2 :{line2}")
except:
    print("Error : The file 'sample.txt' was not found")