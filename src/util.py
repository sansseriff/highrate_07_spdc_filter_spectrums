import csv
import numpy as np
from collections import namedtuple

def load_spectrum_file(filename):
    data = []
    wavelengths = []
    values = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    start_idx = None
    for i in range(len(data)):
        if len(data[i]) >= 3:
            if data[i][0] == "Stop":
                start_idx = i + 3
                break
    if start_idx is None:
        print("Could not find start of data")
    else:
        for i in range(start_idx, len(data)-1):
            wavelengths.append(float(data[i][0]))
            values.append(float(data[i][1]))
    return np.array(wavelengths), np.array(values)


def load_LCS_bands(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        wavelengths = []
        channels = []
        band = []
        for row in csv_reader:
            wavelengths.append(float(row[0]))
            channels.append(int(row[1]))
            band.append(row[2])

    wavelengths = np.array(wavelengths)
    channels = np.array(channels)

    idler_full = wavelengths[wavelengths>1542.94]
    signal_full = np.flip(wavelengths[wavelengths<1536.61])
    idler_full = idler_full[21:]

    return signal_full, idler_full