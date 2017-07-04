# -*- coding: utf-8 -*-

from plone.i18n.normalizer import idnormalizer
from plone import api


def create_architect(name, street, num, postal_code, locality, phone):
    idArchitect = idnormalizer.normalize(name + 'Architect').replace(" ", "")
    containerArchitects = api.content.get(path='/urban/architects')

    if idArchitect not in containerArchitects.objectIds():
        new_id = idArchitect
        if not (new_id in containerArchitects.objectIds()):
            object_id = containerArchitects.invokeFactory('Architect',
                                                            id=new_id,
                                                            name1=name,
                                                            street=street,
                                                            number=num,
                                                            zipcode=postal_code,
                                                            city=locality,
                                                            phone=phone,
                                                          )
