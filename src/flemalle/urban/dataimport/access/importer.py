# -*- coding: utf-8 -*-
from flemalle.urban.dataimport.access import objectsmapping
from flemalle.urban.dataimport.access import valuesmapping
from flemalle.urban.dataimport.access.interfaces import IFlemalleDataImporter
from imio.urban.dataimport.access.importer import AccessDataImporter, AccessImportSource
from imio.urban.dataimport.importsource import DataExtractor
from imio.urban.dataimport.errormessage import ImportErrorMessage
from imio.urban.dataimport.access.interfaces import IAccessImportSource
from imio.urban.dataimport.mapping import ObjectsMapping, ValuesMapping

from zope.interface import implements

import csv
import subprocess


class FlemalleImportSource(AccessImportSource):
    implements(IAccessImportSource)

    def __init__(self, importer):
        super(FlemalleImportSource, self).__init__(importer)
        self.headers, self.header_indexes = self.setHeaders()

    def setHeaders(self):
        command_line = ['mdb-tables', '-d', '"', self.importer.db_path]
        output = subprocess.Popen(command_line, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        table_names = output.stdout.next()
        table_names = table_names.split('"')[:-1]

        headers = {}
        header_indexes = {}

        for table in table_names:
            csv_source = self._exportMdbToCsv(table=table)
            headers[table] = csv_source.next().split(',')
            header_indexes[table] = dict([(headercell.strip(), index) for index, headercell in enumerate(headers[table])])

        return headers, header_indexes

    def iterdata(self):
        csv_source = self._exportMdbToCsv()
        lines = csv.reader(csv_source)
        lines.next()  # skip header
        return lines

    def _exportMdbToCsv(self, table=None):
        table = table or self.importer.table_name
        command_line = ['mdb-export', self.importer.db_path, table]
        csv_export = subprocess.Popen(command_line, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return csv_export.stdout


class AccessDataExtractor(DataExtractor):

    def extractData(self, valuename, line):
        tablename = getattr(self.mapper, 'table_name', self.mapper.importer.table_name)
        datasource = self.datasource

        data = line[datasource.header_indexes[tablename][valuename]]
        return data


class AccessErrorMessage(ImportErrorMessage):

    def __str__(self):
        key = self.importer.getData(self.importer.key_column, self.line)
        migration_step = self.error_location.__class__.__name__
        factory_stack = self.importer.current_containers_stack
        stack_display = '\n'.join(['%sid: %s Title: %s' % (''.join(['    ' for i in range(factory_stack.index(obj))]), obj.id, obj.Title()) for obj in factory_stack])

        message = [
            'line %s (key %s)' % (self.importer.current_line, key),
            'migration substep: %s' % migration_step,
            'error message: %s' % self.message,
            'data: %s' % self.data,
            'plone containers stack:\n  %s' % stack_display,
        ]
        message = '\n'.join(message)

        return message


class FlemalleAccessDataImporter(AccessDataImporter):

    implements(IFlemalleDataImporter)

    def __init__(self, db_name='Urbanisme.mdb', table_name=None, key_column='Noref', savepoint_length=0):
        super(FlemalleAccessDataImporter, self).__init__(db_name, table_name, key_column, savepoint_length)


class FlemalleAccessMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return objectsmapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return objectsmapping.FIELDS_MAPPINGS


class FlemalleValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return valuesmapping.VALUES_MAPS.get(mapping_name, None)
