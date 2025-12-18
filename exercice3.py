import csv
from datetime import datetime

class BatchProcessor:
    def __init__(self, csv_file, log_file):
        self.csv_file = csv_file
        self.log_file = log_file

    def __enter__(self):
        self.f_csv = open(self.csv_file, newline="")
        self.f_log = open(self.log_file, "a")
        self.reader = csv.reader(self.f_csv)
        self.f_log.write(f"[{datetime.now()}] Début du traitement\n")
        return self

    def process(self):
        for row in self.reader:
            self.f_log.write(f"[{datetime.now()}] Traitement : {row}\n")
            print(row)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.f_log.write(f"[{datetime.now()}] Erreur : {exc_val}\n")
        self.f_log.write(f"[{datetime.now()}] Fin du traitement\n")
        self.f_csv.close()
        self.f_log.close()

with BatchProcessor("operations.csv", "journal.log") as bp:
    bp.process()
