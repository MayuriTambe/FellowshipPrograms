import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters
from azure.storage.blob import BlockBlobService, PublicAccess
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.storage.models import Sku
from azure.mgmt.storage.models import SkuName
from azure.mgmt.storage.models import Kind
from dotenv import load_dotenv
from azure.mgmt.datafactory.models import *
from datetime import datetime, timedelta
import time
import uuid

# Creating .env file and store credentials in it
project_folder = os.path.expanduser('/home/admin1/Desktop/AzureKafka')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# Connnecting
subscription_id = os.environ.get(
    'AZURE_SUBSCRIPTION_ID',
    '2f4d6a91-0bf2-4e34-ae1b-6db8bbcf196b') # your Azure Subscription Id

# Creating Credential block
credentials = ServicePrincipalCredentials(
    client_id=os.environ.get('AZURE_CLIENT_ID'),
    secret=os.environ.get('AZURE_CLIENT_SECRET'),
    tenant=os.environ.get('AZURE_TENANT_ID')
)
client = ResourceManagementClient(credentials, subscription_id)

def print_item(group):
    """Print a ResourceGroup instance."""
    print("\tName: {}".format(group.name))
    print("\tId: {}".format(group.id))
    print("\tLocation: {}".format(group.location))
    print("\tTags: {}".format(group.tags))
    print_properties(group.properties)

def print_properties(props):
    """Print a ResourceGroup properties instance."""
    if props and props.provisioning_state:
        print("\tProperties:")
        print("\t\tProvisioning State: {}".format(props.provisioning_state))
    print("\n\n")



WEST_US = "westus"
GROUP_NAME = "azure-sample-group"
resource_group_params = {"location": "westus"}

# Creating Resource Group
print("Create Resource Group")
print_item(client.resource_groups.create_or_update(GROUP_NAME, resource_group_params))

# Creating Storage account
storage_client = StorageManagementClient(credentials, subscription_id)

bad_account_name = 'invalid-or-used-name'
availability = storage_client.storage_accounts.check_name_availability(bad_account_name)
print('The account {} is available: {}'.format(bad_account_name, availability.name_available))
print('Reason: {}'.format(availability.reason))
print('Detailed message: {}'.format(availability.message))

storage_async_operation = storage_client.storage_accounts.create(
    GROUP_NAME,
    'storageaccpython12',
    StorageAccountCreateParameters(
        sku=Sku(name=SkuName.standard_ragrs),
        kind=Kind.storage,
        location='westus'
    )
)
storage_account = storage_async_operation.result()

storage_keys = storage_client.storage_accounts.list_keys(GROUP_NAME, 'storageaccpython12')
storage_keys = {v.key_name: v.value for v in storage_keys.keys}
print('\tKey 1: {}'.format(storage_keys['key1']))
print('\tKey 2: {}'.format(storage_keys['key2']))

# Create the BlockBlockService that is used to call the Blob service for the storage account.
block_blob_service = BlockBlobService(
    account_name='storageaccpython12', account_key='uMn+FjmXQuwlEVQ3nlA4h6U/75GUlpxu3YvR+ojplT16DYOipaVheRwZH33tdoKFUPclTjfG2S8+3XBJaAWtvA==')

# Create a container called 'quickstartblobs'.
container_name = 'quickstartblobs'
block_blob_service.create_container(container_name)

# Set the permission so the blobs are public.
block_blob_service.set_container_acl(
    container_name, public_access=PublicAccess.Container)

# Create a file in Documents to test the upload and download.
local_path = os.path.expanduser("/home/admin1/Desktop/AzureKafka/")
local_file_name = "QuickStart_" + str(uuid.uuid4()) + ".txt"
full_path_to_file = os.path.join(local_path, local_file_name)

# Write text to the file.
file = open(full_path_to_file, 'w')
file.write("Hello, World!")
file.close()

print("Temp file = " + full_path_to_file)
print("\nUploading to Blob storage as blob" + local_file_name)

# Upload the created file, use local_file_name for the blob name.
block_blob_service.create_blob_from_path(
    container_name, local_file_name, full_path_to_file)

# Create A Data Factory
adf_client = DataFactoryManagementClient(credentials, subscription_id)
dataFactory_name = "adfusingpython"
df_resource = Factory(location='eastus')
df = adf_client.factories.create_or_update('azure-sample-group', dataFactory_name, df_resource)
print_item(df)
while df.provisioning_state != 'Succeeded':
        df = adf_client.factories.get('azure-sample-group', dataFactory_name)
        time.sleep(1)