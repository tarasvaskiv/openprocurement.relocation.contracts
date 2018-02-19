# -*- coding: utf-8 -*-
import unittest

from openprocurement.api.tests.base import snitch
from openprocurement.contracting.api.tests.base import test_contract_data
from openprocurement.relocation.contracts.tests.base import ContractOwnershipWebTest
from openprocurement.relocation.contracts.tests.contract_blanks import (
    change_contract_ownership,
    change_contract_ownership_invalid,
    generate_credentials_with_transfer
)


class ContractOwnershipChangeTest(ContractOwnershipWebTest):
    initial_data = test_contract_data
    first_owner = 'broker'
    second_owner = 'broker3'
    test_owner = 'broker3t'
    invalid_owner = 'broker1'
    initial_auth = ('Basic', (first_owner, ''))

    test_change_contract_ownership = snitch(change_contract_ownership)
    test_change_contract_ownership_invalid = snitch(change_contract_ownership_invalid)
    test_generate_credentials_with_transfer = snitch(generate_credentials_with_transfer)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ContractOwnershipChangeTest))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
