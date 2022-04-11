import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]

def linear_search(sequence, number):
    vyskyt = 0
    index = []
    for i, n in enumerate(sequence):
        if n == number:
            vyskyt += 1
            index.append(i)
    slovnik = {
        "position": index,
        "count": vyskyt
    }
    return slovnik

def pattern_search(sequence, pattern):
    position = set()
    index = 0
    while index < len(sequence) - len(pattern):
        if sequence[index:index + len(pattern)] == pattern:
            position.add(index)
        index += 1
    return position





def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    results = linear_search(sequential_data, 0)
    print(results)
    dna = read_data("sequential.json", "dna_sequence")
    print(pattern_search(dna, "ATA"))

if __name__ == '__main__':
    main()