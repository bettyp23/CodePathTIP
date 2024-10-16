#practice demo of class
#yt video

class video:
    #attributes title, url, num comments
    def __init__(self, title, url, num_comments):
        self.title = title
        self.url = url
        self.num_comments = num_comments

cat = video("my cat", "example.com", 175) #sneaks self when class __innit__ doesnt have self
print(cat.title)