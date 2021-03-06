# This file is part carrier_send_shipments_shippypro module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
from trytond.tests.test_tryton import ModuleTestCase
from trytond.tests.test_tryton import suite as test_suite


class CarrierSendShipmentsShippyproTestCase(ModuleTestCase):
    'Test Carrier Send Shipments Shippypro module'
    module = 'carrier_send_shipments_shippypro'


def suite():
    suite = test_suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            CarrierSendShipmentsShippyproTestCase))
    return suite
