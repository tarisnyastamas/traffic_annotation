import textdistance
from nltk.tokenize import word_tokenize

def clean_text_accents(text: str, replacements: dict):
    """
    Converts the input's diacritics to basic accentless format. 
    
    ### Example:
        >>> clean_text_accents('káposzta')\n
        kaposzta

    #### Args:
        text (str): The input text as a string.
        replacements (dict): Contains the replacement mappings

    #### Returns:
        str: The input text with replaced accent characters.

    """

    text = "".join([replacements.get(c, c) for c in text])
    return text

def get_city_name_from_text(text: str):
    """
    Extracts the city name (word with uppercase initial character) from input string.\nIf there are more than one names in the text, it returns the first one.

    ### Example:
        >>> get_city_name_from_text('this guy is from Scranton, he is the president')
        Scranton

    #### Args:
        text (str): The string from which the city name will be extracted.

    #### Returns:
        str: Name of the city from the text.
    """
    cities_list = []
    for word in word_tokenize(text):
        if word[0].isupper() == True and word not in cities_list:
            cities_list.append(word)
    if len(cities_list) == 1:
        return cities_list[0]
    else:
        print("Warning! There is more than 1 city name in the input, returning the first one.")
        print(cities_list)
        return cities_list[0]

def build_city_list_from_dict(cities_dict: dict, verbose: bool = False):
    """
    Builds list with name of cities from the input dictionary. The input should be in the following format:\n
    {\n
        '<city_name>': {\n
            'name_hun': <hungarian_name>,\n
            ...\n
        },\n
        ...\n
    }\n

    #### Args:
        cities_dict (dict): Dictionary which has the corresponding structure and contains the hungarian names and coordinates.
        verbose (bool): If True, writes output messages to the console.

    #### Returns:
        list: Hungarian names from the dictionary (values under 'name_hun' key).
    """
    i = 0
    city_names = []
    for key, value in cities_dict.items():
        city = cities_dict[key]['name_hun']
        city_names.append(city)

        i += 1
    
    if verbose:
        print("Extracted %d city names from dictionary" % i)
    return city_names

def lookup_closest_str(input_str: str, lookup_list: list):
    """
    Returns the element from the loopup_list which is closest to the input_str using Levenshtein distance.

    ### Example:
        >>> fruits = ['banana', 'apple', 'mango']
        >>> lookup_closest_str('baxnana', fruits)
        banana

    #### Args:
        input_str (str): Input string.
        lookup_list (list): Candidate return strings.

    #### Returns:
        str: The closest string to the input from the candidates.
    """

    # min_dist = 9999
    min_dist = float('inf')
    closest_str = ''
    for elem in lookup_list:
        dist = textdistance.levenshtein(elem, input_str)

        if dist < min_dist:
            min_dist = dist
            closest_str = elem
    return closest_str

def extract_coords_from_text(input_str: str, city_names: list, cities_dict: dict, verbose=False):
    """
    Returns the coordinates of the city in the text. The text should contain only one word with a capital starting letter.

    ### Example:
        >>> text = 'piszolyosok a Kolozsvaron az opera mellett'
        >>> 

    #### Args:
        input_str (str): The input string.
        city_names (list): Candidate city names for correct name lookup.
        cities_dict (dict): City names with coordinates.
        verbose (bool): If True, writes output messages to the console.

    #### Returns:
        list: Two element list, containing coordinates of the city from the text.
    """
    city_name_raw = get_city_name_from_text(input_str)
    city_name = lookup_closest_str(city_name_raw, city_names)
    
    if verbose:
        print("Found city name in string: " + city_name)

    coord_x = cities_dict[city_name]['coords_x']
    coord_y = cities_dict[city_name]['coords_y']

    # NOTE: lehet hogy a koordinatakat fel kell cserelni ahhoz, hogy jo helyre tegye a pin-t
    if verbose:
        print("Coords of {}: {}, {}".format(city_name, coord_x, coord_y))
    
    return [coord_x, coord_y]

def extract_event_from_text(input_str: str, events: list, stopwords: list, verbose: bool = False):
    """
    Returns the event from the text using events as a lookup list and Levenshtein distance as a metric.

    ### Example:
        >>> text = 'piszolyosok a Kolozsvaron az opera mellett'
        >>> 

    #### Args:
        input_str (str): The input string.
        events (list): Candidate event names for correct name lookup.
        stopwords (list): Stopwords without accents.
        verbose (bool): If True, writes output messages to the console.

    #### Returns:
        str: The closest string to input_str from the candidate events.
    """
    words: list = word_tokenize(input_str)
    words: list = [w for w in words if w not in stopwords]
    
    event_in_txt: str = ''
    min_dist = float('inf')

    for word in words:
        inner_dict = {}

        for elem in events:
            dist = textdistance.levenshtein(elem, word)
            inner_dict[elem] = dist

            if dist < min_dist:
                min_dist = dist
                event_in_txt = elem

    if verbose:
        print('Found event in text: ' + event_in_txt)
    
    return event_in_txt

def extract_data_from_text(input_text: str, city_names: list, events: list, cities_dict: dict, stopwords: list, verbose: bool = False):
    """
    Extracts event name and coordinates from input text.\n Uses extract_coords_from_text() and extract_event_from_text() functions.

    Args:
        input_text (str): Input string.
        city_names (list): Candidate city names for correct name lookup.
        events (list): Candidate event names for correct name lookup.
        cities_dict (dict): City names with coordinates.
        stopwords (list): Stopwords without accents.
        verbose (bool): If True, writes output messages to the console.

    Returns:
        dict: {
            'event': <event_name>,
            'x_coord': <coord>,
            'y_coord': <coord>
        }
    """
    coords: list = extract_coords_from_text(input_text, city_names, cities_dict)
    event: str = extract_event_from_text(input_text, events, stopwords)
    
    row: dict = {
        'event': event,
        'x_coord': coords[0],
        'y_coord': coords[1]
    }
    
    if verbose:
        print(row)
    
    return row

def main():
    pass

if __name__ == "__main__":
    main()
