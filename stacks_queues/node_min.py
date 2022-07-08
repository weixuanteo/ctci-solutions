class NodeMin:
    def __init__(self, data, min):
        self.data = data
        self.next = None
        self.min = min

    def __str__(self):
        return str(self.data)
