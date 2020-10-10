import os, sys, shutil, compileall

def compile_project(old_proj, new_proj=None):

	if new_proj is None:
		new_proj = old_proj+'_compiled'

	if os.path.exists(new_proj):
		shutil.rmtree(new_proj)
	shutil.copytree(old_proj, new_proj)

	compileall.compile_dir(new_proj)

	for folder, subfolders, files in os.walk(new_proj):
		for file in files:
			if file.endswith('.py'):
				file_name = file[:-3]
				os.remove(os.path.join(folder, file))
				os.rename(
					os.path.join(
						folder, 
						'__pycache__',
						file_name+'.'+sys.implementation.cache_tag+'.pyc'
					),
					os.path.join(folder,file_name+'.pyc')
				)


if __name__ == '__main__':
	
	try:
		old_proj = sys.argv[1]
	except IndexError:
		raise Exception("Missing: project to be compiled")
	try:
		new_proj = sys.argv[2]
	except IndexError:
		new_proj = old_proj+'_compiled'

	compile_project(old_proj, new_proj)