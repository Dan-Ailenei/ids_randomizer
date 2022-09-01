import sys
from bs4 import BeautifulSoup
import string
from itertools import chain
import random


def get_random_id():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(10))


file_name = sys.argv[1]
dest_file = sys.argv[2]


with open(file_name) as fp:
    file_content = fp.read()


soup = BeautifulSoup(file_content, 'html.parser')

ids = {tag['id'] for tag in soup.select('[id]')}

classes = set()
for tag in soup.select('[class]'):
    for klass in tag['class']:
        classes.add(klass)


for attr in chain(ids, classes):
    file_content = file_content.replace(attr, get_random_id())


with open(dest_file, 'w') as f:
    f.write(file_content)
