#!/usr/bin/env python

__author__ = "Kathryn Anderson"

import requests
import turtle
import time

def people_in_space():
    retrieve = requests.get('http://api.open-notify.org/astros.json')
    space = retrieve.json()
    for person in space["people"]:
        print(person["name"] + ",", person["craft"])
    print(f"{person['number']} people in space")




def main():
    pass


if __name__ == '__main__':
    main()
