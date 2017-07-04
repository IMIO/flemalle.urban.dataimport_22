# -*- coding: utf-8 -*-
from imio.urban.dataimport.access.interfaces import IAccessMapper, IAccessImportSource, IAccessImporter


class IFlemalleMapper(IAccessMapper):
    """ marker interface for access mappers """


class IFlemalleImportSource(IAccessImportSource):
    """ marker interface for access import source """


class IFlemalleDataImporter(IAccessImporter):
    """ marker interface for flemalle access importer """

