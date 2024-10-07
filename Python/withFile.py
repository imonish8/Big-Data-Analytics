bytes_data =b"\x21"
try:
    with open(" ", "wb") as fp:
        fp.write(bytes_data)
        fp.close()
except FileNotFoundError:
    print("Create Byte File")
except IOError :
    print("an error occured while reading the file ")

