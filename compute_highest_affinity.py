# No need to process files and manipulate strings - we will
# pass in lists (of equal length) that correspond to
# sites views. The first list is the site visited, the second is
# the user who visited the site.

# See the test cases for more details.

def highest_affinity(site_list, user_list, time_list):
    # Returned string pair should be ordered by dictionary order
    # I.e., if the highest affinity pair is "foo" and "bar"
    # return ("bar", "foo").
    page_pair = dict()
    user_pages = dict()
    max = 0

    pages = set()
    for page in site_list:
        pages.add(page)

    page_list = list(pages)
    page_list.sort()
    print(page_list)

    for i in range(0, len(page_list)):
        for j in range(i+1, len(page_list)):
            page_pair[(page_list[i], page_list[j])] = 0
    print(page_pair)

    for user in user_list:
        user_pages[user] = set()

    for i in range(0, len(user_list)):
        user_pages[user_list[i]].add(site_list[i])

    for pair in page_pair:
        for user in user_pages:
            if pair[0] in user_pages[user] and pair[1] in user_pages[user]:
                page_pair[pair] += 1
                if page_pair[pair] > max:
                    max = page_pair[pair]
                    max_item = pair

    print(page_pair)

    if 1 == 0:
        page_pair = dict()
        user_pages = dict()
        max = 0

        pages = set()
        for page in site_list:
            pages.add(page)

        page_list = list(pages)
        page_list.sort()
        print(page_list)

        for i in range(0, len(page_list)):
            for j in range(i+1, len(page_list)):
                page_pair[(page_list[i], page_list[j])] = 0
        print(page_pair)

        for user in user_list:
            user_pages[user] = set()

        for i in range(0, len(user_list)):
            user_pages[user_list[i]].add(site_list[i])
        for user in user_list:
            user_pages[user] = set()
        for i in range(0, len(user_list)):
            user_pages[user_list[i]].add(site_list[i])
        for user in user_list:
            user_pages[user] = set()

        for i in range(0, len(user_list)):
            user_pages[user_list[i]].add(site_list[i])

        for pair in page_pair:
            for user in user_pages:
                if pair[0] in user_pages[user] and pair[1] in user_pages[user]:
                    page_pair[pair] += 1
                    if page_pair[pair] > max:
                        max = page_pair[pair]
                        max_item = pair

        print(page_pair)


    return max_item
