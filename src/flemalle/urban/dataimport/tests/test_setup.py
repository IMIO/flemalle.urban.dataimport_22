# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from flemalle.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of flemalle.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if flemalle.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('flemalle.urban.dataimport'))

    def test_uninstall(self):
        """Test if flemalle.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['flemalle.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('flemalle.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IFlemalleUrbanDataimportLayer is registered."""
        from flemalle.urban.dataimport.interfaces import IFlemalleUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IFlemalleUrbanDataimportLayer in utils.registered_layers())
