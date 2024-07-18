#!/usr/bin/env python3
""" Test file """

get_page = __import__('web').get_page

if __name__ == "__main__":
    content = get_page("http://slowwly.robertomurray.co.uk")
    print(content)
