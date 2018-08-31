from rawparser import *

if __name__ == '__main__':
    itemList = itemParser(readItemsFile('input.txt'))
    stopWords = readStopWordsFile('filter.txt')

    items = []
    for index, s in enumerate(itemList):
        items.append(Item(index+1, s, filter=stopWords, format=format))

    with open('output.xml', 'w', encoding='utf-8') as f:
        f.write(HEADER)
        for item in items:
            f.write(item.__str__())
        f.write(FOOTER)
