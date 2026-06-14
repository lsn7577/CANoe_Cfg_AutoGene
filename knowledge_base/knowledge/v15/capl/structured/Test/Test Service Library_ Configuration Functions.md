# Test Service Library: Configuration Functions

> Category: `Test` | Type: `notes`

## Description

The functions ChkConfig_Init and ChkConfig_SetPrecision permit node-wide configuration of the TestServiceLibrary.

If the TSL is to be used in Simulation Nodes (not CAPL test modules!), the initialization function ChkConfig_Init should be called. With this function behavior of the TSL in error cases can also be configured there in roughly outlined steps.

The time base of the TSL can be modified for the node in question.

The function ChkConfig_SetTitle permits the configuration of a check.

| Functions | Short Description |
|---|---|
| ChkConfig_DisablePDULayer | Disables the PDU layer for the current bus context. |
| ChkConfig_EnablePDULayer | Enables the PDU layer for the current bus context. |
| ChkConfig_Init | Initializes TSL to be used subsequently. |
| ChkConfig_SetCallback | Sets a CAPL callback for the check. |
| ChkConfig_SetPDUIDFormat | Sets the format of the header ID for the current bus context. |
| ChkConfig_SetPrecision | Configures the TSL time basis for the current node. |
| ChkConfig_SetTitle | Sets the title of a check. |

| Version 15© Vector Informatik GmbH |
|---|
