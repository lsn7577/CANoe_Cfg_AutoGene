# coTfsTimingSDOStart

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsTimingSDOStart( dword nodeId );
```

## Description

The function starts the monitoring of SDO response times. The new values are added to the already saved values. The monitoring can be stopped or paused with coTfsTimingSDOStop.

The monitoring is deactivated for all nodes on measurement start.

## Return Values

Error code

## Example

```c
coTfsTimingSDOStart( 0 ); // start SDO time recording for all nodes
```
