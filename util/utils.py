import json

def load_json(filename: str):
    with open(filename, encoding='UTF-8') as f:
        return json.load(f)

def load_events_from_json(path: str):
    events = []
    events_dict = load_json(path)

    for value in events_dict.values():
        for elem in value:
            events.append(elem)

    return events

def read_file_lines(path:str):
    """
    Reads a file line by line and deletes the newline character from line ends
    
    Returns:
        (list): list of line contents
    """
    lines:list = []
    file = open(path, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        lines.append(line.strip())
    
    return lines

def main():
    pass

if __name__ == '__main__':
    main()