import pathlib
import re
import shutil
import sys
import urllib.request
import zipfile

dependecies_list, i = [], 0


def get_dependencies(plugin):
	global i

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
		elif not line.startswith(' '):
			section = False
		if section:
			plain_str += re.search(r"\S* (.*)", line).groups()[0]

	for item in plain_str.split(','):
		item = item.split(':')[0]
		if item not in dependecies_list:
			dependecies_list.append(item)

	# clean meta directory
	shutil.rmtree('META-INF')

	while i < len(dependecies_list):
		download_plugin(dependecies_list[i])
		i += 1


def download_plugin(plugin):
	download_url = 'https://updates.jenkins-ci.org/latest/'
	plugin += '.hpi'

	if plugin == '.hpi' or pathlib.Path(plugin).is_file():
		return

	print('Download ' + plugin + ' now...')
	urllib.request.urlretrieve(download_url + plugin, plugin)
	get_dependencies(plugin)

if __name__ == '__main__':
	download_plugin(sys.argv[1])
	print('==== Download process is done! ====')
	print('Download List:', dependecies_list)
