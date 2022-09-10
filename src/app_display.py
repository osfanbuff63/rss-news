import sys, os, os.path as path # Main imports
from PySide6.QtWidgets import QApplication, QWidget, QLabel # Qt imports
import qdarktheme # QDarkTheme which I believe has to be imported after Qt

def get_parsed_feeds():
    import parse_feeds, main
    config = main.config_setup()
    parse_feeds.ParseFeed.rss_parse(feeds=rss)

def app_display():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("RSS Feed Notifier")
    window.setGeometry(100, 100, 280, 80)
    window_icon_path = path.abspath(path.join(__file__ ,os.pardir, "../assets/rss.ico"))
    window.setWindowIcon(icon=window_icon_path)
    helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
    helloMsg.move(60, 15)

    # Apply dark theme :tada:
    app.setStyleSheet(qdarktheme.load_stylesheet())

    # Why are windows not shown by default? No one knows...
    window.show()

    # Execute the app loop!
    app.exec()

    return