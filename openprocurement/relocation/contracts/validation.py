# -*- coding: utf-8 -*-
from openprocurement.relocation.core.validation import validate_accreditation_level

def validate_contract_accreditation_level(request):
    validate_accreditation_level(request, request.validated['contract'], 'create_accreditation')
