import os

def reverseFiles(directory=r"."):
    #iterate through the directory 
    for filename in os.listdir(directory):
        #conditional to make sure we only reverse filenames that starts with .data
        if filename.startswith(".data"):
            #creates a new file to be written over, ends with .reversed
            reversedFile = open(f'{filename}.reversed', "w") 
            
            #gives access to read the original file
            originalFile = open(f'{filename}', "r")
            
            #reads and reverses the text of the original file and saves to a variable
            reversedData = originalFile.read()[::-1]

            #save the reversed content onto the reversed file
            reversedFile.writelines(reversedData) 

            #close both original and reversed files
            originalFile.close()
            reversedFile.close()


reverseFiles()
