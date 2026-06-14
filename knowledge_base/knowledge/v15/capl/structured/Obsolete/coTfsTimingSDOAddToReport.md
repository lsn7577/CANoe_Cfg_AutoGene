# coTfsTimingSDOAddToReport

> Category: `Obsolete` | Type: `notes`

## Description

No replacement

| Obsolete Function No replacement |  |
|---|---|
| Function Syntax | long coTfsTimingSDOAddToReport( dword nodeId ); |
| Function | The minimum, maximum and average SDO response time of the specified node are added to the test protocol. The statistic values are not reset. |
| Parameters | nodeId 0: for all nodes 1..127: for a special node |
| Return Values | Error code |
| Example coTfsTimingSDOAddToReport( 0 ); // add all available time statistics to test report |  |

| Version 15© Vector Informatik GmbH |
|---|
