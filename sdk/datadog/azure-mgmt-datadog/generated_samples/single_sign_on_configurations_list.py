# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.datadog import MicrosoftDatadogClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-datadog
# USAGE
    python single_sign_on_configurations_list.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = MicrosoftDatadogClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.single_sign_on_configurations.list(
        resource_group_name="myResourceGroup",
        monitor_name="myMonitor",
    )
    for item in response:
        print(item)


# x-ms-original-file: specification/datadog/resource-manager/Microsoft.Datadog/stable/2022-06-01/examples/SingleSignOnConfigurations_List.json
if __name__ == "__main__":
    main()
