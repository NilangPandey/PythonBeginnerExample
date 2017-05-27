text_file_again = raw_input("Enter your file name\n")
#print text_file_again
txt = open(text_file_again)

print txt.read()
txt.close()
