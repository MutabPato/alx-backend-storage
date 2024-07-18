#!/usr/bin/env python3
""" Test file """

get_page = __import__('web').get_page

if __name__ == "__main__":
    content = get_page("https://www.alxafrica.com")
    print(content)
