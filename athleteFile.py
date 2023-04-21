# Routines to create, write and read athlete data file
# ==================================================== 

# Libraries and modules

import json

# Class definition

class ProcessJsonFile():

    def __init__(self):
        pass

    def saveData(self, file, data):
        """Saves all athlete data to disk

        Args:
            file (str): Name of the file
            data (list): List of dictionaries 

        Returns:
            tuple: Error code, Error message, detailed error message
        """
        status = (0, 'Tallennus onnistui', 'All data saved succesfully')
        return status

    def readData(self, file):
        """Reads athlete data from file

        Args:
            file (str: Name of the file

        Returns:
            tuple: Error code, Error message, detailed error message, data
        """
        data = (0, message, detailedMessage, readinfo)
        return data
    
    def appendDAATA(self, file, data):
        """Adds a new json object to the file

        Args:
            file (str): Name of the file
            data (dict): python dictionary containing

        Returns:
            _tuple: Error code, Error message, detailed error message
        """
        status = (0, 'Tallennus onnistui', 'Data saved successfully')
        return status


# Preliminary tests

if __name__ == "__main__":
    pass