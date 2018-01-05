import logging
import sys

from .application import Application

logging.basicConfig(stream=sys.stderr, level=logging.INFO)

app = Application()
app.execute()
