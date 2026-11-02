import zipfile,os
from pathlib import Path
# print(Path.cwd())

def backup_to_zip(folder):
	folder=Path(folder)
	num=1
	while True:
		zip_filename=Path(folder.parts[-1]+'_'+str(num)+'.zip')

		if not zip_filename.exists():
			break
		num+=1
		
	#zip file	

	backup_zip=zipfile.ZipFile(zip_filename,'w')

	for folder_name, subfolders, filenames in os.walk(folder):
		folder_name=Path(folder_name)
		print(f"adding files to {folder_name}")
		
		rel=folder_name.relative_to(folder)
		if rel !=Path('.'):
			backup_zip.write(folder_name,arcname=rel)
		for filename in filenames:		
			arc=rel/filename

			if filename.startswith('.'):
				continue
			print(f'adding files :{filename}')
			backup_zip.write(folder_name/filename, arcname=arc, compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)

	backup_zip.close()


backup_to_zip(Path.cwd())
# z=zipfile.ZipFile("python_1.zip")
# z.extractall(Path.cwd()/'restore_spam')
# for info in z.infolist():
# 	print(info.filename,info.file_size,info.compress_size)