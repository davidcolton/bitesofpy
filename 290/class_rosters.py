import csv


def class_rosters(input_file):
    """ Read the input_file and modify the data
        according to the Bite description.
        Return a list holding one item per student
        per class, correctly formatted."""
    classes = []
    year = "2020"
    with open(input_file, "r") as f:
        students = csv.reader(f, quotechar='"')
        for student in students:
            s_id = student[0]
            s_classes = student[2:]
            classes.extend(
                [
                    f"{s_class.split(' - ')[0]},{year},{s_id}"
                    for s_class in s_classes
                    if s_class != ""
                ]
            )
    return classes


class_rosters("content.csv")

