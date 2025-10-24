"""Autor: Andre"""
class Album:
    def __init__(self,title,author,tracks):
        self.tracks = tracks
        self.title = title
        self.author = author
    
    def specs(self):
        print( f"This album is {self.title}, {self.author} and have:")