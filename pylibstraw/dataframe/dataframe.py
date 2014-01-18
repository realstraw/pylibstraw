
class DataFrameFile:
    """
    A data frame bind from a csv file
    """
    
    def __init__(self, datafile, header = True):
        if header:
            self.header = header
            self.datafile = file.open(datafile, 'r')
            self.cur_row = 0

    def __iter__(self):
        return self

    def next(self):
        line = self.datafile.readline()
        self.cur_row = self.cur_row + 1

        if len(line) == 0:
            return None
        
        return line[:-1].split(",")
