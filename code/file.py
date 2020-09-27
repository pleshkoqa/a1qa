class File(object):

    def __init__(self, filename, content):
        """
        Construct object with passed filename and content, set extension based
        on filename and calculate size as half content length.

        :param filename: File name (mandatory) with extension (optional), without directory tree (path separators:
     *                 https://en.wikipedia.org/wiki/Path_(computing)#Representations_of_paths_by_operating_system_and_shell)
        :param content: File content (could be empty, but must be set)
        """
        self._filename = filename
        self._content = content
        self._size = len(content) / 2
        self._extension = self._filename.split("\\.")[len(self._filename.split("\\.")) - 1]

    def get_size(self):
        """
        Get exactly file size

        :return: File size
        """

        return int(self._size)

    def get_filename(self):
        """
        Get File filename

        :return: File filename
        """
        return self._filename
