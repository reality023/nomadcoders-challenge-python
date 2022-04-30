from flask import send_file
import csv


def save_to_file(name, jobs):
    file = open(f"{name}.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Link"])
    for job in jobs:
        writer.writerow(list(job.values()))
