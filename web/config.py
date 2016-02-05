# List of all the URLs
import os

LIST_BEACONS = \
    'https://proximitybeacon.googleapis.com/v1beta1/beacons?pageSize=100'

SCOPE = 'https://www.googleapis.com/auth/userinfo.profile \
    https://www.googleapis.com/auth/userlocation.beacon.registry'

REGISTER_BEACONS = \
    'https://proximitybeacon.googleapis.com/v1beta1/beacons:register'

BEACON = 'https://proximitybeacon.googleapis.com/v1beta1/'

DEACTIVATE = ':deactivate'

ACTIVATE = ':activate'

NAMESPACE = 'https://proximitybeacon.googleapis.com/v1beta1/namespaces'

ATTACH = '/attachments'

QUERY = '?namespacedType=*/*'

ERROR = 'ERROR'

BATCH_DELETE = ':batchDelete?namespacedType=*/*'

SUCCESS = 'SUCCESS'

QUERY = '?namespacedType=*/*'

USER_INFO = 'https://www.googleapis.com/oauth2/v1/userinfo'

ESTIMOTE_CMD = \
    "curl -u " + str(os.environ.get('ESTIMOTE_USERNAME')) + ":" + \
    str(os.environ.get('ESTIMOTE_PASSWORD')) + \
    " -H 'Accept: application/json' https://cloud.estimote.com/v1/beacons"
