from nltk.corpus.reader.chasen import test
import pandas as pd
from nltk.corpus import stopwords, util

import util.text_process as tp
import util.utils as utils

#### FUNCTION DEFINITIONS ####
def get_data(text):
    return tp.extract_data_from_text(
        text, 
        city_names, 
        events, 
        cities_dict, 
        hun_stopwords,
        get_city=True
    )
##############################

######### FILE PATHS #########
replacements_file_path = 'data/replacements.json'
events_path = 'data/events.json'
coords_file = 'data/cities_hu_coords.json'
##############################


######## LOADING DATA ########
replacements = utils.load_json(replacements_file_path)

events = utils.load_events_from_json(events_path)
events_dict = utils.load_json(events_path)

cities_dict = utils.load_json(coords_file)
city_names = tp.build_city_list_from_dict(cities_dict)

# get hungarian stopwords and clean accents from them
hun_stopwords = stopwords.words('hungarian')
hun_stopwords = [tp.clean_text_accents(w,replacements) for w in hun_stopwords]
##############################


######### PROCESSING #########
test_text = 'piszolyosok a Kolozsvaron az opera mellett'

# Extract data from text
d = get_data(test_text)
d = utils.change_event_to_categ(d, events_dict)

# Put extracted data into dataframe
df = pd.DataFrame(columns=['city_name', 'event', 'x_coord', 'y_coord'])
df = df.append(d, ignore_index=True)
##############################

print(df)
