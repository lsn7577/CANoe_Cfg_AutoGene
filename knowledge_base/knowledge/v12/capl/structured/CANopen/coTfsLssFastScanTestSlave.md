# coTfsLssFastScanTestSlave

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssFastScanTestSlave( void );
```

## Description

This function executes a LSS FastScan test for CANopen® slaves.

## Return Values

Error code

## Example

```c
if (coTfsLssFastScanTestSlave() == 1) {
  write ("LSS Fast Scan of slaves successfully executed");
}
```
