class StoreName():
    def __init__(self, name, location):
        self.name = name
        self.location = location
    

class Warehouse(StoreName):
    def __init__(self, name, area, size, location):
        StoreName.__init__(self, name, location)
        self.area = area
        self.size = size
        self.type = location


