try:
    file = open("output.txt", "r+")
    content = file.read()
    print(content)
    i = int(content.strip())
    
    print(file.tell())
    #print(file.seek(22))
    print(file.tell())
    file.seek(0)
    file.write("This is new line")
    print(content)
    file.truncate()
    file.close()
    
   
except FileNotFoundError as e:
    print(f" Please run touch Output.txt in working directory  : {e}")
    
except IOError as e :
    print("an error occured : {e}")

except ValueError as e:
    print("error throwing : {e}")
