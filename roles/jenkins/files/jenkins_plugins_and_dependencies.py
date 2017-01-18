import zipfile

# dependecies_list = []


# def get_dependencies():
# 	section, plain_str = False, ""
# 	f = open('/Users/tsoliang/Downloads/META-INF/MANIFEST.MF', 'r')
# 	for line in f:
# 		if line.startswith('Plugin-Dependencies'):
# 			section = True
# 		elif line.startswith('Plugin-Developers'):
# 			section = False
# 		if section:
# 			plain_str += line.rstrip().lstrip('Plugin-Dependencies:').lstrip(' ')

# 	for item in plain_str.split(','):
# 		dependecies_list.append(item.split(':')[0])

# get_dependencies()
# print(dependecies_list)

zip_ref = zipfile.ZipFile('/Users/tsoliang/Downloads/git.hpi', 'r')
zip_ref.extract('META-INF/MANIFEST.MF', '.')
zip_ref.close()
