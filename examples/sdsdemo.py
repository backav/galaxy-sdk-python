import random
import time
import sys

from sds.client.clientfactory import ClientFactory
from sds.client.datumutil import datum
from sds.client.datumutil import values
from sds.client.tablescanner import scan_iter
from sds.auth.ttypes import Credential
from sds.auth.ttypes import UserType
from sds.common.constants import ADMIN_SERVICE_PATH
from sds.common.constants import TABLE_SERVICE_PATH
from sds.common.constants import DEFAULT_ADMIN_CLIENT_TIMEOUT
from sds.common.constants import DEFAULT_CLIENT_TIMEOUT
from sds.errors.ttypes import ServiceException
from sds.errors.constants import ErrorCode
from sds.table.constants import DataType
from sds.table.ttypes import KeySpec, EntityGroupSpec, LocalSecondaryIndexSpec, SecondaryIndexConsistencyMode
from sds.table.ttypes import TableSchema
from sds.table.ttypes import TableQuota
from sds.table.ttypes import TableMetadata
from sds.table.ttypes import TableSpec
from sds.table.ttypes import ProvisionThroughput
from sds.table.ttypes import PutRequest
from sds.table.ttypes import GetRequest
from sds.table.ttypes import ScanRequest

endpoint = "http://awsbj0.sds.api.xiaomi.com"
# Set your AppKey and AppSecret
appKey = "5871752725166"
appSecret = "PWaqc+A/yt9U/JR0Us4w0g=="
credential = Credential(UserType.APP_SECRET, appKey, appSecret)
client_factory = ClientFactory(credential, True)
table_client = client_factory.new_table_client(endpoint + TABLE_SERVICE_PATH,
                                               DEFAULT_CLIENT_TIMEOUT)

table_name = "o2-bikes-geo-index"

# scan by last modify time
print("================= scan by last modify time ====================")
start_key = {'bike_id': datum('0')}
stop_key = start_key
scan = ScanRequest(tableName=table_name,
                   indexName='index_geohash',
                   startKey=start_key,  # None or unspecified means begin of the table
                   stopKey=stop_key,  # None or unspecified means end of the table
                   attributes=['bike_id','latitude', 'longitude'],  # scan all attributes if not specified
                   limit=1)  # batch size

for record in scan_iter(table_client, scan):
    print(record)


