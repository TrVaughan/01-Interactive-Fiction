#!/usr/bin/env python3
import sys,os,json,re
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

def load(l):
    f = open(os.path.join(sys.path[0], l))
    data = f.read()
    j = json.loads(data)
    return j

def find_passage(game_desc, pid):
    for p in game_desc["passages"]:
        if p ["pid"] == pid:
            return p 
    return {}



# Removes Harlowe formatting from Twison description
def format_passage(description):
    description = re.sub(r'//([^/]*)//',r'\1',description)
    description = re.sub(r"''([^']*)''",r'\1',description)
    description = re.sub(r'~~([^~]*)~~',r'\1',description)
    description = re.sub(r'\*\*([^\*]*)\*\*',r'\1',description)
    description = re.sub(r'\*([^\*]*)\*',r'\1',description)
    description = re.sub(r'\^\^([^\^]*)\^\^',r'\1',description)
    description = re.sub(r'(\[\[[^\|]*?)\|([^\]]*?\]\])',r'\1->\2',description)
    description = re.sub(r'\[\[([^(->\])]*?)->[^\]]*?\]\]',r'[ \1 ]',description)
    description = re.sub(r'\[\[(.+?)\]\]',r'[ \1 ]',description)
    return description

def update():
    pass

def render(current):
    print(current["name"])
    print(format_passage(current["text"]))


def get_imput():
    choice = input("What would you like to do? ")
    return choice

def main():
    game_desc = load("game.json")
    current = find_passage(game_desc, game_desc["startnode"])
    choice = ""
    while choice != "quit" and current != {}:
        update()
        render(current)
        choice = get_imput()


print("Thanks for playing!")



if __name__ == "__main__":
  main()