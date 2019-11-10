from os.path import join
from saml2 import BINDING_HTTP_POST
from saml2 import BINDING_HTTP_REDIRECT
from saml2.saml import NAMEID_FORMAT_EMAILADDRESS
from saml2.saml import NAMEID_FORMAT_UNSPECIFIED
from saml2.sigver import get_xmlsec_binary
from settings.base import DEBUG
from settings.base import BASE_DIR

LOGIN_URL = '/login/'
BASE_URL = 'http://localhost:9000/idp'

SAML_IDP_CONFIG = {
    'debug' : DEBUG,
    'xmlsec_binary': get_xmlsec_binary(['/opt/local/bin', '/usr/bin/xmlsec1']),
    'entityid': '%s/metadata' % BASE_URL,
    'description': 'Kileed SAML IDP',
    'service': {
        'idp': {
            'name': 'Django localhost IdP',
            'endpoints': {
                'single_sign_on_service': [
                    ('%s/sso/post' % BASE_URL, BINDING_HTTP_POST),
                    ('%s/sso/redirect' % BASE_URL, BINDING_HTTP_REDIRECT),
                ],
            },
            'name_id_format': [
                NAMEID_FORMAT_EMAILADDRESS,
                NAMEID_FORMAT_UNSPECIFIED
            ],
            'sign_response': True,
            'sign_assertion': True,
        },
    },

    'metadata': {
        'local': [join(BASE_DIR, 'idp', 'saml2_config', 'sp_metadata.xml')],
    },

    'key_file': BASE_DIR + '/dev/snakeoil.key',
    'cert_file': BASE_DIR + '/dev/snakeoil.crt',
    'encryption_keypairs': [{
        'key_file': BASE_DIR + '/dev/snakeoil.key',
        'cert_file': BASE_DIR + '/dev/snakeoil.crt',
    }],
    'valid_for': 365 * 24,
}

SAML_IDP_SPCONFIG = {
    'http://localhost:8000/idp/metadata/': {
        'processor': 'djangosaml2idp.processors.BaseProcessor',
        'attribute_mapping': {
            # DJANGO: SAML
            'email': 'email',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'is_staff': 'is_staff',
            'is_superuser':  'is_superuser',
        }
    }
}
