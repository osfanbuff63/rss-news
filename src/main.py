## Functions ##
def config_setup(self):
    import os, os.path as path, configparser
    config_path = path.abspath(path.join(__file__ ,os.pardir, "../config/rss.cfg"))
    config = configparser.ConfigParser
    config.read(filenames=config_path,self=self)
    rss = config["RSS Feeds"]["rss"]
    print("config setup")
    return rss

## Main triggers ##

