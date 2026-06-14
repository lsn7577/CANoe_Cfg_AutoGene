# coTfsNmt

> Category: `CANopen` | Type: `function`

## Syntax

```c
coTfsNmt () != 1);
```

## Description

This function attempts to set the following device states in the DUT Device Under Test sequentially: Stop, Reset, Operational, Pre-Operational, Reset Communication, Start, Pre-Operational and Reset.

After this test, the DUT is in the pre-operational state.

If the heartbeat producer is already active, it will be restored at the end.

## Return Values

Error code

## Example

```c
if ( coTfsNmt () != 1) { 
  write ("coTfsNMT failed");
}
```
