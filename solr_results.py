from SolrClient import SolrClient
import pandas as pd
import spacy
import matplotlib.pyplot as plt
import random

texts = []

def solr_search(text):
    # Connect to the solr server
    url = "http://localhost:8983/solr"
    solr = SolrClient(url)

    # Store collection name in a variable
    collection = 'uscis'

    # Create a list of schema items
    schema = ["Employer",
            "NAICS",
            "State",
            "City",
            "ZIP",
            "id",
            "Fiscal_Year",
            "Initial_Approvals",
            "Initial_Denials",
            "Continuing_Approvals",
            "Continuing_Denials",
            "Tax_ID",
            "_version_"]

    # Load English tokenizer, tagger, parser, NER and word vectors
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    state = ''
    year = ''
    employer = ''
    query = ''
    abbr = ''

    # Find named entities, phrases and concepts
    for entity in doc.ents:
    #     print(entity.text, entity.label_)
        if entity.label_ == 'GPE':
            state = entity.text.title()
            if state == 'Alabama' or state == 'Al':
                abbr = 'AL'
            elif state == 'Alaska' or state == 'Ak':
                abbr = 'AK'
            elif state == 'Arizona' or state == 'Az':
                abbr = 'AZ'
            elif state == 'Arkansas' or state == 'Ar':
                abbr = 'AR'
            elif state == 'California' or state == 'Ca':
                abbr = 'CA'
            elif state == 'Colorado' or state == 'Co':
                abbr = 'CO'
            elif state == 'Connecticut' or state == 'Ct':
                abbr = 'CT'
            elif state == 'Delaware' or state == 'De':
                abbr = 'DE'
            elif state == 'Florida' or state == 'Fl':
                abbr = 'FL'
            elif state == 'Georgia' or state == 'Ga':
                abbr = 'GA'
            elif state == 'Hawaii' or state == 'Hi':
                abbr = 'HI'
            elif state == 'Idaho' or state == 'Id':
                abbr = 'ID'
            elif state == 'Illinois' or state == 'Il':
                abbr = 'IL'
            elif state == 'Indiana' or state == 'In':
                abbr = 'IN'
            elif state == 'Iowa' or state == 'Ia':
                abbr = 'IA'
            elif state == 'Kansas' or state == 'Ks':
                abbr = 'KS'
            elif state == 'Kentucky' or state == 'Ky':
                abbr = 'KY'
            elif state == 'Louisiana' or state == 'La':
                abbr = 'LA'
            elif state == 'Maine' or state == 'Me':
                abbr = 'ME'
            elif state == 'Maryland' or state == 'Md':
                abbr = 'MD'
            elif state == 'Massachusetts' or state == 'Ma':
                abbr = 'MA'
            elif state == 'Michigan' or state == 'Mi':
                abbr = 'MI'
            elif state == 'Minnesota' or state == 'Mn':
                abbr = 'MN'
            elif state == 'Mississippi' or state == 'Ms':
                abbr = 'MS'
            elif state == 'Missouri' or state == 'Mo':
                abbr = 'MO'
            elif state == 'Montana' or state == 'Mt':
                abbr = 'MT'
            elif state == 'Nebraska' or state == 'Ne':
                abbr = 'NE'
            elif state == 'Nevada' or state == 'Nv':
                abbr = 'NV'
            elif state == 'New Hampshire' or state == 'Nh':
                abbr = 'NH'
            elif state == 'New Jersey' or state == 'Nj':
                abbr = 'NJ'
            elif state == 'New Mexico' or state == 'Nm':
                abbr = 'NM'
            elif state == 'New York' or state == 'Ny':
                abbr = 'NY'
            elif state == 'North Carolina' or state == 'Nc':
                abbr = 'NC'
            elif state == 'North Dakota' or state == 'Nd':
                abbr = 'ND'
            elif state == 'Ohio' or state == 'Oh':
                abbr = 'OH'
            elif state == 'Oklahoma' or state == 'Ok':
                abbr = 'OK'
            elif state == 'Oregon' or state == 'Or':
                abbr = 'OR'
            elif state == 'Pennsylvania' or state == 'Pa':
                abbr = 'PA'
            elif state == 'Rhode Island' or state == 'Ri':
                abbr = 'RI'
            elif state == 'South Carolina' or state == 'Sc':
                abbr = 'SC'
            elif state == 'South Dakota' or state == 'Sd':
                abbr = 'SD'
            elif state == 'Tennessee' or state == 'Tn':
                abbr = 'TN'
            elif state == 'Texas' or state == 'Tx':
                abbr = 'TX'
            elif state == 'Utah' or state == 'Ut':
                abbr = 'UT'
            elif state == 'Vermont' or state == 'Vt':
                abbr = 'VT'
            elif state == 'Virginia' or state == 'Va':
                abbr = 'VA'
            elif state == 'Washington' or state == 'Wa':
                abbr = 'WA'
            elif state == 'West Virginia' or state == 'Wv':
                abbr = 'WV'
            elif state == 'Wisconsin' or state == 'Wi':
                abbr = 'WI'
            elif state == 'Wyoming' or state == 'Wy':
                abbr = 'WY'
            elif state == 'District Of Columbia' or state == 'Washington Dc' or state == 'Dc':
                abbr = 'DC'
            elif state == 'Marshall Islands' or state == 'Mh':
                abbr = 'MH'
            elif state == 'Armed Forces Africa' or state == 'Armed Forces Canada' or state == 'Armed Forces Europe' or state == 'Armed Forces Middle East' or state == 'Ae':
                abbr = 'AE'
            elif state == 'Armed Forces Americas' or state == 'Aa':
                abbr = 'AA'
            elif state == 'Armed Forces Pacific' or state == 'Ap':
                abbr = 'AP'
        elif entity.label_ == 'DATE':
            try:
                year = int(entity.text)
            except Exception as e:
                print(e)
        elif entity.label_ == 'PERSON' or entity.label_ == 'ORG':
            try:
                employer = entity.text.title()
            except Exception as e:
                print(e)

    # Creating empty string variables for each schema item
    naics = ''
    city = ''
    zip_ = ''
    id_ = ''
    initial_approvals = ''
    initial_denials = ''
    continuing_approvals = ''
    continuing_denials = ''
    tax_id = ''
    _version_ = ''

    # Creating a list of values for each schema item
    # schema_val_lst = [employer, naics, state, city, zip_, id_, year, initial_approvals, initial_denials, continuing_approvals, continuing_denials, tax_id, _version_]

    # Create a list of arguments within the query
    # query = []
    # for s, l in zip(schema, schema_val_lst):
    #     if l != '':
    #         query.append(s+':'+l)

    # # Concatenating the query arguments into a single string
    # query = ' '.join(query)

    if employer != '':
        query = 'Employer:'+employer

    # If-else condition to populate the correct query
    if query == '':
        query = '*:*'
    # print(query)

    # Creating variables for other query arguments for solr.query
    fq = None
    facet = True
    facet_pivot = 'Fiscal_Year, State'
    # facet_range = None
    # facet_range_start = None
    # facet_range_end = None
    # facet_range_gap = None

    # Running the solr query and storing in a variable named 'res'
    res = solr.query(collection,
                    {'q':query,
                    'fq':fq,
                    'facet':facet,
                    'facet.pivot':facet_pivot,
    #                   'facet.range':facet_range,
    #                   'facet.range.start':facet_range_start,
    #                   'facet.range.end':facet_range_end,
    #                   'facet.range.gap':facet_range_gap,
                    })

    facet_pivot = res.get_facet_pivot()
    # How many record were found?
    # print("Numfound: ", res.get_num_found())
    # print("Facets: ", res.get_facet_pivot())

    years = []
    states = []
    counts = []
    for keys, values in facet_pivot.items():
        for key, value in values.items():
            for k, v in value.items():
                years.append(key)
                states.append(k.upper().strip())
                counts.append(v)
    df = pd.DataFrame({'Year': years,'State': states,'Count': counts})

    results = ["Seems like I don't have the answer to all your questions!",
              "You should try again with a different question",
              "Give me a break man",
              "Who do you think I am? I ofcourse don't know what you're asking about",
              "Try again",
              "That's the wrong question, probably you whould learn how to question"]
    result = random.choice(results)
    
    # Case 1
    if state == '' and employer == '' and year != '':
        try:
            count = sum(df[df['Year']==year].sort_values(by=['State']).reset_index(drop=True)['Count'])
            result = 'In ' + str(year) + ', ' + str(count) + ' visas were issued in total across the USA.'
        except Exception as e:
            print(e)
            pass
    # Case 2
    elif state != '' and employer == '' and year == '':
        try:
            count = sum(df[df['State']==abbr].sort_values(by=['Year']).reset_index(drop=True)['Count'])
            result = 'In ' + state + ', ' + str(count) + ' visas have been issued from 2009-2019.'
        except Exception as e:
            print(e)
            pass
    # Case 3
    elif state != '' and employer == '' and year != '':
        try:
            count = df[df['State']==abbr].set_index('Year').get_value(year, 'Count')
            result = 'In ' + str(year) + ', ' + str(count) + ' visas were issued in ' + state + '.'
        except Exception as e:
            print(e)
            pass
    # Case 4
    elif state != '' and employer != '' and year == '':
        try:
            count = df[df['State']==abbr].set_index('Year').get_value(year, 'Count')
            result = 'In ' + state + ', ' + employer + ' has been issued ' + str(count) + ' visas.'
        except Exception as e:
            print(e)
            pass
    # Case 5
    elif state == '' and employer != '' and year != '':
        try:
            count = sum(df[df['Year']==year].sort_values(by=['State']).reset_index(drop=True)['Count'])
            result = 'In ' + str(year) + ', ' + str(count) + ' visas were issued to ' + employer + '.'
        except Exception as e:
            print(e)
            pass
    # Case 6
    elif state == '' and employer != '' and year == '':
        try:
            result = employer + ' has been issued ' + str(res.get_num_found()) + ' visas between 2009-2019.'
        except Exception as e:
            print(e)
            pass
    else:
        result = result

    return result