# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.resourceconnector import Appliances

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-resourceconnector
# USAGE
    python appliances_create_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = Appliances(
        credential=DefaultAzureCredential(),
        subscription_id="11111111-2222-3333-4444-555555555555",
    )

    response = client.appliances.begin_create_or_update(
        resource_group_name="testresourcegroup",
        resource_name="appliance01",
        parameters={
            "location": "West US",
            "properties": {"distro": "AKSEdge", "infrastructureConfig": {"provider": "VMWare"}},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/resourceconnector/resource-manager/Microsoft.ResourceConnector/stable/2022-10-27/examples/AppliancesCreate_Update.json
if __name__ == "__main__":
    main()
