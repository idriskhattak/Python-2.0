# A dictionary inside a dictionary

Dict = {
    'name':{
        'stnd_1': 'Idris',
        'stnd_2': 'Khan',
        'stnd_3': 'Khattak'
    },
    'grades':{
        'stnd_1': 'A-',
        'stnd_2': 'B+',
        'stnd_3': 'A+'
    }
}

print(Dict['name']['stnd_1'])

# Dictionay Methods
print(Dict.keys()) # Priting just the keys in Dict
print(Dict.values())  # Priting just the values in Dict
print(Dict.items())  # Priting both the keys and values in Dict
print(Dict['name']['stnd_1'])