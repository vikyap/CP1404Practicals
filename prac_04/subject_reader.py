FILENAME = "subject_data.txt"


def get_data():
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        data.append(parts)
    input_file.close()
    return data


def display_subject_details(data):
    for subject_details in data:
        print("{} is taught by {:12} and has {:3} students".format(*subject_details))


def main():
    data = get_data()
    display_subject_details(data)



main()