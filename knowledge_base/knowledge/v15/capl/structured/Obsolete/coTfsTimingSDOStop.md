# coTfsTimingSDOStop

> Category: `Obsolete` | Type: `notes`

## Description

This function is replaced by coTfsMonitorDeactivate.

| Obsolete Function This function is replaced by coTfsMonitorDeactivate. |  |
|---|---|
| Function Syntax | long coTfsTimingSDOStop( dword nodeId ); |
| Function | The function stops the monitoring of SDO response times. The already saved values are not lost. The monitoring can be resumed with coTfsTimingSDOStart(). |
| Parameters | nodeId 0: for all nodes 1..127: for a special node |
| Return Values | Error code |
| Example coTfsTimingSDOStop( 0 ); // stop SDO time recording for all nodes |  |

| Version 15© Vector Informatik GmbH |
|---|
