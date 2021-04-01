import numpy
import os
import sys

null = None

class UserInput:
	InputTypeHash = dict(
		{
			"affirmative" : numpy.array(list(["yes",  "y"]))
		}
	)

	def IsAffirmative(userInput: str):	#	Checks if the provide user input string exists in the array hashed to the affirmative key
		return (userInput.lower() in UserInput.InputTypeHash["affirmative"])

class FileIO:
	def CreateFile(filePath: str):	#	Creates a file at the provided file path
		open(filePath, 'w')

	def PushToFile(buffer: str, filePath: str):		#	Concats the existing string read from the given file with the provided string, and pushes is back to the file
		Buffer = str()
		FileBuffer = str()

		try:
			FilePointer = open(filePath, "r+")
			FileBuffer = FilePointer.read()

			if (FileBuffer == str()):
				Buffer = f"{str(FilePointer.read())}{buffer}"
			else:
				Buffer = f"{str(FilePointer.read())}\n{buffer}"

			print(Buffer)

			FilePointer.write(Buffer)
		
		except FileNotFoundError:
			print(f"{filePath} was not found.")
			
			if (UserInput.IsAffirmative(input("Do you want to create one?"))):
				FileIO.CreateFile(f"{os.getcwd()}/docfile")

		return bool(1)

class Docfile:
	DefaultFileName = str("docfile")

	def GetDocumentPoints():
		DocfilePoints = numpy.ndarray

		FilePointer = null

		try:
			FilePointer = open(Docfile.DefaultFileName, 'r')
		
		except FileNotFoundError:
			FileIO.CreateFile(f"{os.getcwd()}/docfile")
			FilePointer = open(Docfile.DefaultFileName, 'r')
		
		DocfilePoints = numpy.array(list(str(FilePointer.read()).split('\n')))

		# print(len(DocfilePoints))

		return len(DocfilePoints)#(len(list(str(FilePointer.read()).split('\n'))) - 1)

	def AddDocumentPoint(docPoint: str):
		DocSize = Docfile.GetDocumentPoints()

		print(DocSize)

		FileIO.PushToFile(f"{DocSize}. {docPoint}", f"{os.getcwd()}/{Docfile.DefaultFileName}")

		return bool(1)

def Main():
	Docfile.AddDocumentPoint(sys.argv[1])

Main()
