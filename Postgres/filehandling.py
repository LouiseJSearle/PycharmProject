# imports

import requests


# function : create directory

def createDir(location, name):


# function : list files

def listFiles(directory):


## File Object :

class DataFile:
    """A generic data file"""
    def __init__(self):
        self.url = ''
        self.data = None
        self.type = None
        self.name = ''
        self.location = ''

# method : download file

    def download(self, address):
        self.url = str(address)
        response = requests.get(self.url)
        return

# method : write file

    def writeFile(self, data, name, type):
        return

# method : read file

    def readFile(self, file):
        return

# method : move file

    def moveFile(self, file, location):
        return

# method : delete file

    def deleteFile (self, file):
        return
