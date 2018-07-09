import os

from ditto.writers.gridlabd.write import writer as Writer
from ditto.readers.Synergi.SynergiDittoReader_Debug import reader as Reader

from ditto.store import Store
from tests import ditto_dir


m = Store()
reader = Reader()

reader.parse(m)

writer = Writer()
writer.write(m)