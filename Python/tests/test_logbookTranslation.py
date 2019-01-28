import arrow
from dateutil import tz
from aaLogbook import xmlTranslation, logbookTranslation
from pathlib import Path
from importlib import resources


def test_Arrow():
    dt = arrow.get("2016-10-20T18:15:00")
    print("\n", dt)
    dt2 = arrow.get(dt.datetime, tz.gettz('America/New_York'))
    print(dt2)
    dt3 = dt.replace(tzinfo="America/New_York")
    print(dt3)


def loadXml():
    xmlPath = pathToDataDirectory() / Path('myCrystalReportViewer.xml')
    parsedXML = xmlTranslation.parseXML(xmlPath)
    return parsedXML


def pathToDataDirectory()->Path:
    with resources.path('tests', 'resources') as filePath:
        return filePath


def translateParsedXml():
    parsed = loadXml()
    translated = logbookTranslation.buildLogbook(parsed)
    return translated


def test_translatedLogToStdOut():
    print(translateParsedXml())