import re

txt = "Learn Python Through Tutorials of JavaScript"

search_object = re.search(r'(.*p?) (.*o?)(.*h)', txt)

if search_object:
	print("search object group ", search_object.group())
	print("search object group 1", search_object.group(1))
	print("search object group 2", search_object.group(2))
	
else:
	print("Found Nothing")

