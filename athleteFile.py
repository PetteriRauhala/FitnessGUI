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
        try:
            with open(file, 'w') as fileToWrite:
                json.dump(data, fileToWrite, indent=4)
            status = (0, 'Tallennus onnistui :)', 'All data saved succesfully')
        except Exception as error:
            status = (1, 'Tallennus ei onnistunut :(', str(error))
        return status

    def readData(self, file):
        """Reads athlete data from file

        Args:
            file (str: Name of the file

        Returns:
            tuple: Error code, Error message, detailed error message, data
        """
        # Read previous athlete_data from disk
        with open(file, 'r') as fileToRead:
            athlete_data = json.load(fileToRead)
            message = 'OK'
            detailedMessage = 'Data read successfully from disk'
            data = (0, message, detailedMessage, athlete_data)
        return data
    
    def appendDATA(self, file, data):
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