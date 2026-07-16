# filer=open("output.txt",'xt')
# writ=input("Enter text to write to the file:")
# filer.write(writ)
# print("Data successfully written to output.txt \n")

# filer.close()



file=open("output.txt",'at')
v=input("\n Enter additional text to append:")
file.write(v)
print("Data successfully appended.")
file.close()

