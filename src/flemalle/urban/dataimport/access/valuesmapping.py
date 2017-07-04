# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapping import table

VALUES_MAPS = {

    'type_map': table({
    'header'  : ['portal_type',         'foldercategory', 'abreviation'],
    'B'       : ['BuildLicence',        'uap',            'BL'],
    'L'       : ['ParcelOutLicence',    '',               'PL'],
    'D'       : ['Declaration',         '',               'DU'],
    'T'       : ['MiscDemand',          '',                'T'],
    'P'       : ['MiscDemand',          '',                'P'],
    'C'       : ['UrbanCertificateOne', '',               'C1'],
    'V'       : ['NotaryLetter',        '',               'NL'],
    }),


    'eventtype_id_map': table({
    'header'             : ['decision_event', 'folder_complete'],
    'BuildLicence'       : ['delivrance-du-permis-octroi-ou-refus', 'accuse-de-reception'],
    'ParcelOutLicence'   : ['delivrance-du-permis-octroi-ou-refus', 'accuse-de-reception'],
    'Declaration'        : ['deliberation-college', 'accuse-de-reception'],
    'UrbanCertificateOne': ['octroi-cu1', 'accuse-de-reception'],
    'UrbanCertificateTwo': ['octroi-cu2', 'accuse-de-reception'],
    'MiscDemand'         : ['deliberation-college', 'accuse-de-reception'],
    'EnvClassOne'        : ['decision', 'accuse-de-reception'],
    'EnvClassTwo'        : ['decision', 'accuse-de-reception'],
    'EnvClassThree'      : ['acceptation-de-la-demande', 'accuse-de-reception'],
    'NotaryLetter'       : ['octroi-lettre-notaire', ''],
    }),

    'documents_map': {
        'BuildLicence': 'URBA',
        'UniqueLicence': 'PERMIS-UNIQUE',
        'ParcelOutLicence': 'LOTISSEMENT',
        'Declaration': 'REGISTRE-PU',
        'UrbanCertificateOne': 'CU/1',
        'UrbanCertificateTwo': 'CU/2',
        'MiscDemand': 'AUTRE DOSSIER',
        'EnvClassOne': 'ENVIRONNEMENT',
        'EnvClassTwo': 'ENVIRONNEMENT',
        'EnvClassThree': 'ENVIRONNEMENT',
    },

    'titre_map': {
        'monsieur': 'mister',
        'messieurs': 'misters',
        'madame': 'madam',
        'mesdames': 'ladies',
        'mademoiselle': 'miss',
        'monsieur et madame': 'madam_and_mister',
    },

    'externaldecisions_map': {
        'F': 'favorable',
        'FC': 'favorable-conditionnel',
        'D': 'defavorable',
        'RF': 'favorable-defaut',
    },

    'division_map': {
        "1": "62037",
        "2": "62502",
        "3": "62083",
        "4": "62412",
        "5": "62007",
        "6": "62402",
        "7": "62055",
        "8": "62072",
        "9": "62036",
    },

}
