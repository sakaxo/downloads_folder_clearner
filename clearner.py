from watchdog.events import FileSystemEventHandler
from os.path import splitext, isfile,exists
from watchdog.observers import Observer
from os import listdir
import shutil
import time



file_format_types = {
"audio":[
			'.mp3', '.wma','.m4a','.aac','.mid','.ogg',
			'.flac','.wav','.amr','.aiff'
		],

"image":[
			'.jpg','.png','.jpeg','.dwg','.xcf','.jpx',
			'.apng','.gif','.webp','.cr2','.tif','.tiff',
			'.jxr','.psd','.ico','.heic','.avif','.eps',
			'.bmp',
		],

"document":[
			'.pdf','.docx','.doc','.odt','.xls','.xlsx',
			'.ods','.ppt','.pptx','.odp','.txt',
		],

"video":[
			'.mp4'
		],

}

path_to_destination = {
	"audio": 'C:/Users/SEB/Desktop/Dowloaded files/audio',
	"image": 'C:/Users/SEB/Desktop/Dowloaded files/images',
	"document": 'C:/Users/SEB/Desktop/Dowloaded files/documents',
	"video": 'C:/Users/SEB/Desktop/Dowloaded files/video',
	"uncategorised": 'C:/Users/SEB/Desktop/Dowloaded files/uncategorised',
	
}

# folder_to_track 	= 'C:/Users/SEB/Desktop/keepTrack'



def move_file(src,dst):
	"""
	Move file from source directory (src) to a destination 
	directory (dst) and  rename it if the file already exists at
	the specified destination before moving it

	"""

	i = 0
	file_exists = exists(dst)

	while file_exists:
		i += 1

		name,ext = splitext(dst)

		new_name = name + " copy " + "(" + str(i) + ")" + ext


		if not exists(new_name):

			dst = new_name
			break

	shutil.move(src,dst)
	


folder_to_track = "C:/Users/SEB/Downloads"

class MyEventHandler(FileSystemEventHandler):
	
	def on_modified(self,event):
		
		for file in listdir(folder_to_track):

			source_path = folder_to_track + '/' + file
			ext = splitext(file)[1] # get extension

			#deal with files only and skip folders
			if isfile(source_path):

				if ext in file_format_types["audio"]: #audio file

					dest_path = path_to_destination["audio"] + '/' + file
					move_file(src=source_path,dst=dest_path)

					

				elif ext in file_format_types["image"]: #image file
					
					dest_path = path_to_destination["image"] + '/' + file
					move_file(src=source_path,dst=dest_path)


				elif ext in file_format_types["document"]: # documents

					dest_path = path_to_destination["document"] + '/' + file
					move_file(src=source_path,dst=dest_path)


				elif ext in file_format_types["video"]: # video

					dest_path = path_to_destination["video"] + '/' + file
					move_file(src=source_path,dst=dest_path)


				else:  # unknown type of file

					dest_path = path_to_destination["uncategorised"] + '/' + file
					move_file(src=source_path,dst=dest_path)

						


event_handler = MyEventHandler()

observer = Observer()

observer.schedule(event_handler,folder_to_track,recursive=False)
observer.start()

try:
	print("monitoring..")
	while  True:
		time.sleep(5)
		
except KeyboardInterrupt:
	observer.stop()
	print("done")

observer.join()
