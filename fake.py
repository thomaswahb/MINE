from faker import Faker
import csv

f = Faker()
info = ["name", "job", "email", "phone", "country", "salary"]
data = []


def title(name, rows):
    with open(name, "w") as w:
        file = csv.DictWriter(w, fieldnames=info)
        file.writeheader()
        for i in range(int(rows)):
            data_dict = {}

            data_dict["name"] = f.name()
            data_dict["job"] = f.job()
            data_dict["email"] = f.free_email()
            data_dict["phone"] = f.phone_number()
            data_dict["country"] = f.country()
            data_dict["salary"] = f.random_int(min=3000, max=15000)

            data.append(data_dict)
        file.writerows(data)


name = input("name :  ")
num = input("num :  ")

title(name, num)
