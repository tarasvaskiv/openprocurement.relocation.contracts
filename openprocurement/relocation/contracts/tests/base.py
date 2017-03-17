# -*- coding: utf-8 -*-
import os
from copy import deepcopy
from openprocurement.relocation.core.tests.base import BaseWebTest


class ContractOwnershipWebTest(BaseWebTest):
    relative_to = os.path.dirname(__file__)

    def setUp(self):
        super(ContractOwnershipWebTest, self).setUp()
        self.create_contract()

    def create_contract(self):
        data = deepcopy(self.initial_data)

        orig_auth = self.app.authorization
        self.app.authorization = ('Basic', ('contracting', ''))
        response = self.app.post_json('/contracts', {'data': data})
        self.contract = response.json['data']
        # self.contract_token = response.json['access']['token']
        self.contract_id = self.contract['id']
        self.app.authorization = orig_auth
