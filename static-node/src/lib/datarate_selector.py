DATARATE_SEQUENCE = [5, 4, 5, 3, 5, 4, 5, 2, 5, 4, 5, 3, 5, 4, 5, 1, 5, 4, 5, 3,
                     5, 4, 5, 2, 5, 4, 5, 3, 5, 4, 5, 0, 5, 4, 5, 3, 5, 4, 5, 2,
                     5, 4, 5, 3, 5, 4, 5, 1, 5, 4, 5, 3, 5, 4, 5, 2, 5, 4, 5, 3,
                     5, 4, 5]


def select_datarate(index):
    """ Provides LoRaWAN datarate to use. """
    return DATARATE_SEQUENCE[index % len(DATARATE_SEQUENCE)]
