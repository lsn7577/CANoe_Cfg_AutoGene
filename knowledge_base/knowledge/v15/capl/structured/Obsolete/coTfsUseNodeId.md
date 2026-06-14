# coTfsUseNodeId

> Category: `Obsolete` | Type: `notes`

## Description

No replacement.

See Also

| Obsolete Function No replacement. |  |
|---|---|
| Function Syntax | long coTfsUseNodeId( void ); |
| Function | This function instructs the node layer, for functions which accept both the node-ID and the CAN-ID as parameter, to use the node-ID. This setting is active automatically on measurement start. |
| Parameters | — |
| Return Values | Error code |
| Example coTfsUseNodeId();// uses node-ID for simplified functions// …coTfsUseCANid();// uses can identifier for simplified functions// … |  |

| Version 15© Vector Informatik GmbH |
|---|
