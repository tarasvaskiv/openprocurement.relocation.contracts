# -*- coding: utf-8 -*-
from openprocurement.api.utils import (
    json_view,
    APIResource,
    ROUTE_PREFIX,
    context_unpack
)
from openprocurement.contracting.api.utils import (
    contractingresource, save_contract
)
from openprocurement.relocation.core.utils import change_ownership
from openprocurement.relocation.core.validation import validate_set_or_change_ownership_data
from openprocurement.relocation.contracts.validation import validate_contract_accreditation_level


@contractingresource(name='Contract ownership',
                     path='/contracts/{contract_id}/ownership',
                     description="Contracts Ownership")
class ContractResource(APIResource):

    @json_view(permission='view_contract',
               validators=(validate_contract_accreditation_level,
                           validate_set_or_change_ownership_data,))
    def post(self):
        contract = self.request.validated['contract']

        if contract.status != "active":
            self.request.errors.add('body', 'data', 'Can\'t update credentials in current ({}) contract status'.format(contract.status))
            self.request.errors.status = 403
            return

        location = self.request.route_path('Contract', contract_id=contract.id)
        location = location[len(ROUTE_PREFIX):]  # strips /api/<version>
        if change_ownership(self.request, location) and save_contract(self.request):
                self.LOGGER.info('Updated ownership of contract {}'.format(contract.id),
                                 extra=context_unpack(self.request, {'MESSAGE_ID': 'contract_ownership_update'}))

                return {'data': contract.serialize('view')}
