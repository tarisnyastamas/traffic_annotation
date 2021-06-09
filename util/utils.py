import json

def load_json(filename: str):
    with open(filename, encoding='UTF-8') as f:
        return json.load(f)

def read_file_lines(path):
    """
    Reads a file line by line and deletes the newline character from line ends
    
    Returns:
        (list): list of line contents
    """
    lines = []
    file = open(path, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        lines.append(line.strip())
    
    return lines