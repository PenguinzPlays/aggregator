#!/usr/bin/python

class csvmanipulator:


    def __init__(self):
        pass


    def csvinput(self, filepath, headers):
        from csv import DictReader
        try:
            with open(filepath, 'r') as csvfile:
                csvdict = DictReader(csvfile, fieldnames=headers)
                return csvdict
        except Exception as err:
            print("CSV IN: error reading file: %s" % err)
        return  False

    def csvoutput(self, aggdict, filepath, headers):
        from csv import DictWriter
        try:
            with open(filepath, 'w') as csvfile:
                writer = DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(aggdict)
            return True
        except Exception as err:
            print("CSV IN: error reading file: %s" % err)
            return False

    def aggregator(self, comparedictA, comparedictB):
        combineddict = []
        try:
            for rowA in comparedictA:
                for rowB in comparedictB:
                    tempdict = {}
                    if rowB['ip'] in rowA['ip']:
                        tempdict.update(rowB)
                        tempdict.update(rowA)
                        combineddict.append(tempdict)
            return combineddict
        except Exception as err:
            print("CSV IN: error reading file: %s" % err)
            return False

def main(filepath1, filepath2, headers1, headers2):
    dictA = csvmanipulator.csvinput(filepath1)
    dictB = csvmanipulator.csvinput(filepath2)
    dictX = csvmanipulator.aggregator(dictA,dictB)

if __name__ == "__main__":
    from os import path
    filepath1 = path("c:","path","file1.csv")
    filepath2 = path("c:", "path", "file2.csv")
    headers1 = ["header1","header2"]
    headers2 = ["header1", "header2"]
    main(filepath1, filepath2, headers1, headers2)
