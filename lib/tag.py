class Tag:
    def __init__(self, id, name, post = []):
        self.id = id
        self.name = name
        self.post = post
        

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        
    def __repr__(self):
        return f"Tag({self.id}, {self.name})"