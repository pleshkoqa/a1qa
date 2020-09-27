# encoding=utf8
import time

from file_already_exist_error import FileAlreadyExistError


class FileStorage(object):

    def __init__(self, size=0):
        """
        Construct object and set max storage size and available size according passed values (default value ==100)

        :param size: FileStorage size
        """
        self._max_size = self._available_size = 100
        self._files = []
        self._max_size = size
        self._available_size += self._max_size

    def write(self, file):
        """
        Write file in storage if filename is unique and size is not more than available size

        :param file: to save in file storage
        :return: result of file saving

        :raise: FileAlreadyExistError in case of already existent filename
        :
        """

        if self.is_exists(file.get_filename()):
            raise FileAlreadyExistError
        if file.get_size() >= self._available_size:
            return False

        self._files.append(file)
        self._available_size -= file.get_size()
        return True

    def is_exists(self, filename):
        """
        Check is file exist in storage

        :param filename to search
        :return: result of checking
        """
        for file in self._files:
            if filename in file.get_filename():
                return True
        return False

    def delete(self, filename):
        """
        Delete file from storage

        :param filename of file to delete
        :return: result of file deleting
        """
        self._files.remove(self.get_file(filename))

    def get_file(self, filename):
        """
        Get file by filename

        :param: fileName of file to get
        :return: file
        """
        if self.is_exists(filename):
            for file in self._files:
                if file.get_filename() == filename:
                    return file
        return None