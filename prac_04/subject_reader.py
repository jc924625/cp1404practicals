"""
CP1404/CP5632 Practical
Data file -> lists program
"""
FILENAME = "subject_data.txt"
def main():
    """start of program"""
    data = get_data()
    print(data)
    print_data(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    new_list = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts(notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that is  working
        new_list.append(parts)
    input_file.close()
    return new_list

def print_data(data):
    """display subject lecturer and number of students """
    for subject in data:
        print("{} is taught by {:2} and has {:3} students.".format(*subject))
main()