import PyPDF2 as pd

filename = input('Path to the file: ')
file = open(filename,'rb')
pdfReader = pd.PdfReader(file)

tried = 0

if not pdfReader.is_encrypted:
    print('The file is not password protected! You can successfully open it!')
else:
    wordListFile=open("wordsList.txt","r",errors="ignore")
    body=wordListFile.read().lower()
    words=body.split("\n")
    for i in range(len(words)):
        word=words[i]
        print(f"try to decode passward by {word}")
        result=pdfReader.decrypt(word)
        if result==1:
            print("success the passward is " + word)
            break
        elif result==0:
            tried+=1
            print("password tried "+str(tried))
            continue




            


