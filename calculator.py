import argparse
from random import randint
skill = 40
distance = 200

hit_percent = min(100, ((skill/2) + max(0, (100-distance*2))) + randint(0, 12))

print(int(hit_percent))
