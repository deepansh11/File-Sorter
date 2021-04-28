import glob2,shutil,os,time,pyfiglet

result = pyfiglet.figlet_format("File Sorter")
print(result)

list = ["pdf","docx","pptx","xlsx","jpg","png","jpeg","exe","mp4","txt"]
path_name = input("[+] Enter the absolute path you want file sorter to work on: ")

def store_files(name,number):
    data = []
    temp = list[number]
    for child in glob2.glob(name+'/*.'+temp):
        data.append(child)
    return data
try:
    for i in range(len(list)):
        child = store_files(path_name,i)
        if glob2.glob(path_name):
            #Check if Downloads folder exist
            if glob2.glob(path_name+'/'+list[i].upper()):
                #use shutil to move all the pdf files to the pdf folder
                if glob2.glob(path_name+'**/*.'+list[i]):
                    for j in child:
                        shutil.move(j,path_name+'/' + list[i].upper())
                    print("Files moved to their respective folders")
                else:
                    print(f"All files are already arranged in {list[i].upper()} folder")

            else:
                path = os.path.join(path_name,list[i].upper())
                print(f"[+] Folder {list[i].upper()} does not exists, So I'm creating one on your behalf...")
                time.sleep(2)
                os.mkdir(path)
                for j in child:
                    shutil.move(j,path_name+'/' + list[i].upper())
                print(f"[+] Folder created and files moved to {list[i].upper()} folder")
        else:
            print("[+] The path you mentioned does not exists, please enter the path again carefully")
except error as e:
    print(e)
