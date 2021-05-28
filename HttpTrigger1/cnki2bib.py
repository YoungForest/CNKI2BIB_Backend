import pyperclip
import logging
import os

from .BibTexEntries import BibTeXContentStringFactory
from .cnkiNetEntries import CNKINetEntryFactory
from .Configure import setIDFormat


def getBibFileContentString(cnkiNetFileContent):
    cnkiNetEntries = CNKINetEntryFactory().giveAllEntries(cnkiNetFileContent)
    return BibTeXContentStringFactory.giveBibFileContentString(cnkiNetEntries)
