import csv


def read_file(file, header=None):
        """
        Loads list from csv file.
        Args: file (str with file's path)
              header (if set to not None returns first line of file with data structure)
        Returns: imported_list[1:] (2d list from file)
        """
        imported_list = []
        with open(file, 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            for line in reader:
                imported_list.append(line)
        if header:
            return imported_list[0]
        return imported_list[1:]
