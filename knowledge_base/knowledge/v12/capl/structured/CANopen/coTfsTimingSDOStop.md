# coTfsTimingSDOStop

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsTimingSDOStop( dword nodeId );
```

## Description

The function stops the monitoring of SDO response times. The already saved values are not lost. The monitoring can be resumed with coTfsTimingSDOStart().

## Return Values

Error code

## Example

```c
coTfsTimingSDOStop( 0 ); // stop SDO time recording for all nodes
```
