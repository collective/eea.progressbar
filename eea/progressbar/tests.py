""" Tests
"""
import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()

import eea.progressbar


class TestCase(ptc.PloneTestCase):
    """ Test case
    """
    class layer(PloneSite):
        """ Layer
        """
        @classmethod
        def setUp(cls):
            """ Setu
            """
            fiveconfigure.debug_mode = True
            ztc.installPackage(eea.progressbar)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            """ Tear dow
            """
            pass


def test_suite():
    """ Suite
    """
    return unittest.TestSuite([

        # Unit tests
        doctestunit.DocFileSuite(
            'README.txt', package='eea.progressbar',
            setUp=testing.setUp, tearDown=testing.tearDown),

        doctestunit.DocFileSuite(
            'docs/exportimport.txt', package='eea.progressbar',
            setUp=testing.setUp, tearDown=testing.tearDown),

        doctestunit.DocTestSuite(
            module='eea.progressbar.interfaces',
            setUp=testing.setUp, tearDown=testing.tearDown),

        # Integration tests that use PloneTestCase
        #ztc.ZopeDocFileSuite(
        #    'README.txt', package='eea.progressbar',
        #    test_class=TestCase),

        #ztc.FunctionalDocFileSuite(
        #    'browser.txt', package='eea.progressbar',
        #    test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
