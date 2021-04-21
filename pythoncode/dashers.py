"""
Find top k dashers closest to a given store. 
Sort key 1: Distance from store (lesser is better)
Sort key 2: Dasher rating (more is better)
"""
import random
import heapq
import unittest

from random import randint
class Dasher(object):
    def __init__(self, store_location, location, rating):
        self.store_location = store_location
        self.location = location
        self.rating = rating
        self.distance_from_store = round((((store_location[0] - location[0]) ** 2 + (store_location[1] - location[1]) ** 2)) ** .5, 2)

    def __lt__(self, other):
        if self.distance_from_store < other.distance_from_store:
            return False
        elif self.distance_from_store > other.distance_from_store:
            return True
        elif self.rating >= other.rating: # at this point distance from store is equal
            return False
        else:
            return True
    
    def __eq__(self, other):
        if self.distance_from_store == other.distance_from_store and self.rating == other.rating:
            return True
        return False
        
    def __str__(self):
        return str((self.distance_from_store, self.rating))

    def __repr__(self):
        return str((self.distance_from_store, self.rating))

# experimental code commented out
# dasher1 = Dasher((3, 4), (1,2), 800)
# print(dasher1)
# dasher2 = Dasher((3, 4), (6,1), 800)
# print(dasher2)

# if dasher1 > dasher2:
#     print(dasher1)
# else:
#     print(dasher2)


def get_dashers(nums):
    dashers = []
    random.seed(1)
    store_location = (3, 4)
    for ele in range(nums):
        location =  (randint(1, 20), randint(1, 20))
        rating = randint(500, 1000)
        dashers.append(Dasher(store_location, location, rating))
    return dashers

def topk_dashers(dashers, k):
    topk = dashers[:k]
    heapq.heapify(topk) # O(k)
    for dasher in dashers[k:]: #O(n-k)
        heapq.heappushpop(topk, dasher) #O(k)
    return sorted(topk) # ascending order #O(klogk)
    # Overall time: O(k) + (n-k) * O(k) + O(klogk) 
    # Overall time: ~ O(n)
    # Overall space: ~ O(k) to maintain the heap of k elements

k = 10
dashers = get_dashers(100)
topk_dashers = topk_dashers(dashers, k)

t = unittest.TestCase()

t.assertEqual(max(dashers), max(topk_dashers))
t.assertEqual(max(dashers), topk_dashers[-1])
t.assertEqual(sorted(dashers)[-1], topk_dashers[-1])
t.assertNotEqual(min(dashers), min(topk_dashers))

t.assertEqual(sorted(dashers)[-1], max(dashers))
t.assertEqual(sorted(dashers)[0], min(dashers))

# More test cases follow ...
