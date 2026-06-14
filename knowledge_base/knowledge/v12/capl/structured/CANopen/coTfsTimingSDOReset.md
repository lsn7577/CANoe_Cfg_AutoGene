# coTfsTimingSDOReset

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsTimingSDOReset( dword nodeId );
```

## Description

The function resets the internal statistics of the SDO response times of the specified node.

## Return Values

Error code

## Example

```c
coTfsTimingSDOReset( 0 ); // reset all sdo time statistics
```
