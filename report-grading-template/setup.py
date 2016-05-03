import zipfile,os.path,os,shutil,sys


def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            # Path traversal defense copied from
            # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                drive, word = os.path.splitdrive(word)
                head, word = os.path.split(word)
                if word in (os.curdir, os.pardir, ''): continue
                path = os.path.join(path, word)
            zf.extract(member, path)



def organize_files():
	files = os.listdir("./reports_original")
	os.makedirs("./reports_workspace")
	for name in sorted(files):
		dirname = ((name.partition(',')[0]).rpartition('-')[0]).strip();
		src = './reports_original/' + name
		dst = './reports_workspace/'+ dirname + '/(commented)' + name
		new_dir_name = "./reports_workspace/" + dirname
		if os.path.exists(new_dir_name):
			shutil.rmtree(new_dir_name)
		os.makedirs(new_dir_name)
		shutil.copy(src, dst)
		shutil.copy("./default_response/eval.mks", "./reports_workspace/" + dirname + "/eval.mks")
		shutil.copy("./default_response/format.mks", "./reports_workspace/" + dirname + "/format.mks")
		shutil.copy("./default_response/finalize.py", "./reports_workspace/" + dirname + "/finalize.py")
		shutil.copytree("./default_response/feedback", "./reports_workspace/" + dirname + "/feedback")

def clean():
	shutil.rmtree('./reports_original')
	shutil.rmtree('./reports_workspace')
	
def main():
	if len(sys.argv) != 2:
		print "Usage: python setup.py [zipfile|\"clean\"]"
		exit(0)
	if sys.argv[1] == "clean":
		while True:
			response = raw_input("Are you sure you want to clean the workspace: [y/n] ")
			if response == "y":
				clean()
				break
			elif response == "n":
				break
			else:
				print "Please answer either \'y\' or \'n\'."
	else:
		os.makedirs("./reports_original")
		unzip(sys.argv[1], "./reports_original")
		if os.path.isfile("./reports_original/index.html"):
			os.remove("./reports_original/index.html")
			organize_files()

main()