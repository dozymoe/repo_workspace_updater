import logging
import sys

from .application import Application

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

app = Application()
app.execute()
