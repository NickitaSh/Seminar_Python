import csv
import re


def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for i in range(1, 4):
        file_name = f"info_{i}.txt"
        with open(file_name, "r") as f:
            data = f.read()

            os_prod = re.findall("Изготовитель ОС:\s+(.*)", data)[0].strip()
            os_name = re.findall("Название ОС:\s+(.*)", data)[0].strip()
            os_code = re.findall("Код продукта:\s+(.*)", data)[0].strip()
            os_type = re.findall("Тип системы:\s+(.*)", data)[0].strip()

            os_prod_list.append(os_prod)
            os_name_list.append(os_name)
            os_code_list.append(os_code)
            os_type_list.append(os_type)

    main_data = [["System manufacturer", "OS Name", "Product code", "System type"]]

    for i in range(len(os_prod_list)):
        data_row = [os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]]
        main_data.append(data_row)

    return main_data


def write_to_csv(csv_file):
    data = get_data()

    with open(csv_file, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


write_to_csv("report.csv")
