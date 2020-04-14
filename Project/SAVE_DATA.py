import csv


class SaveData:

    def __init__(self, data=None, name_of_file='tempCSV'):
        if data is None:
            data = [[0, 0, 0, 0, 0, 0]]
        self.data = data
        self.name_of_file = name_of_file.upper() + 'DELETE_IT.csv'

    def saveDataInCSVFile(self):
        with open(self.name_of_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'original_price', 'discounted_price', 'rating', 'rating_number', 'link'])
            for d in self.data:
                if int(d[1].replace(',', '')) == -1:
                    d[1] = d[2]
                if int(d[2].replace(',', '')) == -1:
                    d[2] = d[1]
                writer.writerow([d[0], d[1], d[2], d[3], d[4], d[5]])

    def appendDataInCSVFile(self):
        with open(self.name_of_file, 'a', newline='') as file:
            writer = csv.writer(file)
            for d in self.data:
                if int(d[1].replace(',', '')) == -1:
                    d[1] = d[2]
                if int(d[2].replace(',', '')) == -1:
                    d[2] = d[1]
                writer.writerow([d[0], d[1], d[2], d[3], d[4], d[5]])
