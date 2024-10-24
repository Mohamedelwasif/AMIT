class TextFileReader:
    """Class to encapsulate functionality for reading and analyzing a text file."""

    def __init__(self, file_path):
        """Initialize with the file path."""
        self.file_path = file_path
        self.content = ""

    def read_file(self):
        """Reads the contents of the file and stores it in the content attribute."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.content = file.read()
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def count_lines(self):
        """Returns the number of lines in the file."""
        if self.content:
            return len(self.content.splitlines())
        return 0

    def count_words(self):
        """Returns the total number of words in the file."""
        if self.content:
            words = self.content.split()
            return len(words)
        return 0

    def count_characters(self):
        """Returns the total number of characters in the file."""
        if self.content:
            return len(self.content)
        return 0

    def display_content(self):
        """Displays the content of the file."""
        if self.content:
            print(self.content)
        else:
            print("The file content is empty. Make sure to call read_file() first.")
