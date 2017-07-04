# -*- coding: utf-8 -*-
from flemalle.urban.dataimport.access.importer import FlemalleAccessDataImporter
from imio.urban.dataimport.access.interfaces import IAccessImporter
from imio.urban.dataimport.browser.adapter import ImporterFromSettingsForm
from imio.urban.dataimport.browser.import_panel import ImporterSettings

from zope.interface import implements


class AccessImporterSettings(ImporterSettings):
    """
    """


class FlemalleImporterFromImportSettings(ImporterFromSettingsForm):
    implements(IAccessImporter)

    def __init__(self, settings_form, importer_class=FlemalleAccessDataImporter):
        """
        """
        super(FlemalleImporterFromImportSettings, self).__init__(settings_form, importer_class)

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(FlemalleImporterFromImportSettings, self).get_importer_settings()

        table_name_map = {
            'access licences custom': 'Permis',
            'access licences custom DeclaUrb': 'DeclaUrb',
        }

        table_init_name = table_name_map[self.form_datas['selected_importer']]

        db_settings = {
            'db_name': 'Urbanisme.mdb',
            'table_name': table_init_name,
        }

        settings.update(db_settings)

        return settings
