# EthGetAdapterStatus

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Deprecated Function Replaced by ethGetLinkStatus |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long EthGetAdapterStatus(); |  |  |  |
| Function | This function reads the state of the Ethernet interface. |  |  |  |
| Parameters | — |  |  |  |
| Return Values | 0: unknown state 1: not connected 2: connected error code |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 7.2-12.0 | Ethernet | — | • |  |
| Example switch (EthGetAdapterStatus()){ case 0: write("Adapter status unknown"); break; case 1: write("Adapter is not connected”); break; case 2: write("Adapter is connected”); break;} |  |  |  |  |

| Version 15© Vector Informatik GmbH |
|---|
