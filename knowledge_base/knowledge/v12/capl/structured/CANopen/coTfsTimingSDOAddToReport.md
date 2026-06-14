# coTfsTimingSDOAddToReport

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsTimingSDOAddToReport( dword nodeId );
```

## Description

The minimum, maximum and average SDO response time of the specified node are added to the test protocol. The statistic values are not reset.

## Return Values

Error code

## Example

```c
coTfsTimingSDOAddToReport( 0 ); // add all available time statistics to test report
```
