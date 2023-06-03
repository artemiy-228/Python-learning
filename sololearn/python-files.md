## Opening Files

	You can use Python to read and write the contents of files.
	Text files are the easiest to manipulate. Before a file can
	be edited, it must be opened, using the <open> function
	
	- myfile = open("filename.txt")

## Opening Files - Modes
	
	You can specify the mode used to open a file by applying a second argument to the open function.
	- Sending "r" means open in read mode, which is the default.
	- Sending "w" means write mode, for rewriting the contents of a file.
	- Sending "a" means append mode, for adding new content to the end of the file.

	Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
	For example:

	- write-mode - open("filename.txt", "w")
	- readmode - open("filename.txt") or open("filename.txt", "r")
	- binary write mode open("filename.txt", "wb")

## Opening Files - Close
	Once a file has been opened and used, you should close it
	This is done with the <close> method of the file object

	- file.close()



## Reading Files

	The conten of a file that has been opened in text mode can be read using the <read> method
	
	file = open("filename.txt")
	example = file.read()
	file.close()

## Reading Files - read atributes
	To read only a certain amount of a file, you can provide a number as an argument to the read function.
 	This determines the number of bytes that should be read.
	You can make more calls to read on the same file object to read more of the file byte by byte.
 	With no argument, read returns the rest of the file.

	file = open("filename.txt")
	print(file.read(16))
	print(file.read(32))
	file.close()


## Reading Files - empty string

	After all contents in a file have been read,
 	any attempts to read further from that file will return an empty string,
 	because you are trying to read from the end of the file.


## Reading Files - read line
	
	To retrieve each line in a file, you can use the readlines method
	 to return a list in which each element is a line in the file.

	 file = open("filename.txt")
	page = file.readlines() - page is list