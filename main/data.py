import os
from main import app
import frontmatter
import glob
dirname = "data/"

def get_items(**kwargs):
    bookmarks = []
    for filename in glob.glob(dirname + "*.md"):
        data = frontmatter.load(filename)
        if 'type' in kwargs:
            if (data['type'] == kwargs['type']):
                bookmarks.append(data)
        else:
            bookmarks.append(data)
    return bookmarks

def create(contents, title):
    with open(dirname + title + ".md", 'w') as f:
        f.write(contents)

def get_item(id):
    print(id)
    return frontmatter.load(glob.glob(f"{dirname}{id}-*.md")[0])
