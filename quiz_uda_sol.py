class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self, item):
        self.items.append(item)

    def getClassiness(self):
        classiness = 0
        if len(self.items) > 0:
            for item in self.items:
                if item == "tophat":
                    classiness += 2
                elif item == "bowtie":
                    classiness += 4
                elif item == "monocle":
                    classiness += 5
        return classiness
