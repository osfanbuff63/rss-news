import feedparser

class ParseFeed():
    def __init__(self) -> None:
        pass
    
    def rss_parse(feeds):
        import feedparser
        for f in feeds:
            parsed_feeds = parsed_feeds+feedparser.parse(f)
        