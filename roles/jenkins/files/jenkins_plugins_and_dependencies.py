import pathlib
import shutil
import sys
import urllib.request
import zipfile

dependecies_list, download_url = [], "https://updates.jenkins-ci.org/latest/"


def get_dependencies(plugin):
	# unzip plugin file
	zip_ref = zipfile.ZipFile(plugin, 'r')
	zip_ref.extract('META-INF/MANIFEST.MF', '.')
	zip_ref.close()

	# analyze plugin dependencies list
	section, plain_str = False, ""
	f = open('META-INF/MANIFEST.MF', 'r')
	for line in f:
		if line.startswith('Plugin-Dependencies'):
			section = True
		elif line.startswith('Plugin-Developers'):
			section = False
		if section:
			plain_str += line.rstrip().lstrip('Plugin-Dependencies:').lstrip(' ')

	for item in plain_str.split(','):
		item = item.split(':')[0]
		if item not in dependecies_list:
			dependecies_list.append(item)

	# clean meta directory
	shutil.rmtree('META-INF')

	i = 0
	while i < len(dependecies_list):
		if not pathlib.Path(item).is_file():
			download_plugin(item)
		i += 1


def download_plugin(plugin):
	print('Now downloading ' + plugin + '...')
	plugin += ".hpi"
	urllib.request.urlretrieve(download_url + plugin, plugin)
	get_dependencies(plugin)

if __name__ == '__main__':
	download_plugin(sys.argv[1])
