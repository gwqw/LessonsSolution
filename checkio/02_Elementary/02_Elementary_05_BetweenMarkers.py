def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    open_item = text.find(begin)
    close_item = text.find(end)
    open_ex = True
    close_ex = True
    if open_item < 0:
        open_item = 0
        open_ex = False
    if close_item < 0:
        close_item = len(text)-1
        close_ex = False
    if open_item > close_item: res = ''
    elif open_ex and close_ex:
        res = text[open_item+len(begin):close_item]
    elif open_ex:
        res = text[open_item+len(begin):]
    elif close_ex:
        res = text[:close_item]
    else:
        res = text
    return res


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
