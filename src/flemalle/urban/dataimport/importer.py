# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.access.importer import AccessDataImporter
from flemalle.urban.dataimport.interfaces import IFlemalleDataImporter


class FlemalleDataImporter(AccessDataImporter):
    """ """

    implements(IFlemalleDataImporter)
