import shutil 
#src_path = "/Users/imonish8/Desktop/t2/test1.txt " #not working
src_path = r"/Users/imonish8/Desktop/Big-Data-Analytics/helloMSG.txt "
#src_path = "Output.txt" #working
des_path = r"/Users/imonish8/Desktop/ "

try:
    shutil.copytree(src_path,des_path)
    print("success")
except FileNotFoundError as e:
    #print(f"FileNotFound Message here : {e}")
    print("Failed")

