from nltk.corpus.reader.chasen import test
import pandas as pd
from nltk.corpus import stopwords

import util.text_process as tp
import util.utils as utils

def get_data(text):
    return tp.extract_data_from_text(
        text, 
        city_names, 
        events, 
        cities_dict, 
        hun_stopwords
    )

# get hungarian stopwords and clean accents from them
# TODO: read replacements from external file
replacements = {
    "Á": "A",
    "É": "E",
    "á": "a",
    "é": "e",
    "í": "i",
    "Ó": "O",
    "ó": "o",
    "Ö": "O",
    "ö": "o",
    "Ő": "O",
    "ő": "o",
    "Ú": "U",
    "ú": "u",
    "Ű": "U",
    "ű": "u",
    "ü": "u",
    "Í": "I"
}

# TODO: read events from external file
events = [
    'baleset',
    'dugo',
    'torlodas',
    'medve',
    'maci',
    'radar',
    'rendor',
    'pisztolyos'
]

hun_stopwords = stopwords.words('hungarian')
hun_stopwords = [tp.clean_text_accents(w,replacements) for w in hun_stopwords]

# load JSON with cities
coords_file = 'cities_hu_coords.json'
cities_dict = utils.load_json(coords_file)

city_names = tp.build_city_list_from_dict(cities_dict)

test_text = 'piszolyosok a Kolozsvaron az opera mellett'
# coords = tp.extract_coords_from_text(test_text, city_names, cities_dict)
# print(coords[0], coords[1])

# event = tp.extract_event_from_text(test_text, events, hun_stopwords, verbose=True)

data_row = tp.extract_data_from_text(
    test_text, 
    city_names, 
    events, 
    cities_dict, 
    hun_stopwords
)



d = get_data(test_text)

df = pd.DataFrame(columns=['event', 'x_coord', 'y_coord'])
df = df.append(d, ignore_index=True)

print(df)
