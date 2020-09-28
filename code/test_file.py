import pytest
from file import File

class Test_File_Module(object):

    def test_filename(self):
        file = File("filename", "content")
        assert file.get_filename() == ("filename"), 'Return correct filename'

    def test_get_size(self):
        file = File("filename", "content")
        assert file.get_size() == len("content"), "Incorrect size"

    def test_get_content(self):
        file = File("filename", "content")
        assert file.get_content() == ("content"), "Contect returning"
