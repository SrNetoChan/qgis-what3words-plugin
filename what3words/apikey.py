from PyQt4.QtCore import QSettings
from PyQt4.QtGui import QInputDialog
from qgis.utils import iface

_apikey = None

def apikey(ask = True):
    global _apikey
    if _apikey is None:
        _apikey = QSettings().value("/what3words/apikey/", None)
        if _apikey is None and ask:
            askForApiKey()
    return _apikey

def askForApiKey():
    global _apikey
    text, ok = QInputDialog.getText(iface.mainWindow(), 'what3words', 'Enter the API Key:')
    if ok:
        _apikey = text
        QSettings().setValue("/what3words/apikey/", text)
