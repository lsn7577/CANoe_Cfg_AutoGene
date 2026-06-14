# LocalSecurityActivateTxPDUs

> Category: `Obsolete` | Type: `notes`

## Description

Replaced by SecurityLocalActivateTxPDUs.

Allows a node (e.g. gateway) to do a CMAC calculation for Tx Secured-I-PDUs of another node.

| Deprecated Function Replaced by SecurityLocalActivateTxPDUs. |  |  |  |  |
|---|---|---|---|---|
| Function Syntax | long LocalSecurityActivateTxPDUs(char[] NodeName) |  |  |  |
| Function | Allows a node (e.g. gateway) to do a CMAC calculation for Tx Secured-I-PDUs of another node. |  |  |  |
| Parameters | NodeName Name of the other node |  |  |  |
| Return Values | 1: Activation successful 0: Specified node is already activated -1: Specified node is null or empty -10: Security is not usable |  |  |  |
| Availability | Up to Version | Restricted To | Measurement Setup | Simulation/Test Setup |
| 11.0 SP2 | CAN CAN FD FlexRay Ethernet | — | • |  |

| Version 15© Vector Informatik GmbH |
|---|
