#
# Assignment5 Interface
# Name: Ali Sarabi
#

from pymongo import MongoClient
import os
import sys
import json


def FindBusinessBasedOnCity(cityToSearch, saveLocation1, collection):
    with open(saveLocation1, "w") as f:

        for bidx in collection.find({'city': {'$regex': cityToSearch, '$options': 'i'}}):
            f.write(str(bidx['name'].upper()) + "$" + str(bidx['full_address'].upper()) + "$" +
                    bidx['city'].upper() + "$" + bidx['state'].upper())
            f.write('\n')
        f.close()
    pass

def FindBusinessBasedOnLocation(categoriesToSearch, myLocation, maxDistance, saveLocation2, collection):
    import string
    with open(saveLocation2, "w") as f:
        for bidx in collection.find({'categories': {'$in': categoriesToSearch}}):
            distance = DistanceFunction(float(bidx["latitude"]),float(bidx["longitude"]),
                                        float(myLocation[0]),float(myLocation[1]))
            if distance<=maxDistance:
                f.write(str(bidx['name'].upper()))
                f.write('\n')
    pass

def DistanceFunction(lat2, lon2, lat1, lon1):
    import math
    R = 3959
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)
    delta_phi = math.radians(lat2-lat1)
    delta_lambda = math.radians(lon2-lon1)
    a = (math.sin(delta_phi/2) * math.sin(delta_phi/2)) + (math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda/2)
                                                           * math.sin(delta_lambda/2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c

    return d