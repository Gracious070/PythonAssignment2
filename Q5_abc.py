from abc import ABC, abstractmethod


class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFileHandler(FileHandler):

    def read(self):
        print("Reading a text file.")

    def write(self, data):
        print("Writing text:", data)


class BinaryFileHandler(FileHandler):

    def read(self):
        print("Reading a binary file.")

    def write(self, data):
        print("Writing binary data:", data)


# Create objects of the concrete classes.
text_handler = TextFileHandler()
binary_handler = BinaryFileHandler()

text_handler.read()
text_handler.write("Hello")

binary_handler.read()
binary_handler.write(b"101010")