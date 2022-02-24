def display_function(toponym_longitude, toponym_lattitude, spn):
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join(spn),
        "l": "map",
        "pt": ','.join([toponym_longitude, toponym_lattitude])
    }
    return map_params
