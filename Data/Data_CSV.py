import csv


class CSV_Manager():
    def __init__(self, path):
        self.path = path


    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path



    def csv_writer(self, data):
        with open(self.path, "wb") as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in data:
                writer.writerow(line)

    def csv_append(self, data):
        with open(self.path, "a") as csv_file:
            writer = csv.writer(csv_file, delimiter=';')
            for line in data:
                writer.writerow(line)



