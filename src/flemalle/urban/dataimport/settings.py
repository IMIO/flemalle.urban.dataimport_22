# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.access.settings import AccessImporterFromImportSettings


class FlemalleImporterSettingsForm(ImporterSettingsForm):
    """ """

class FlemalleImporterSettings(ImporterSettings):
    """ """
    form = FlemalleImporterSettingsForm


class FlemalleImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = FlemalleImporterSettings


class FlemalleImporterFromImportSettings(AccessImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(FlemalleImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': '',
        }

        settings.update(db_settings)

        return settings
