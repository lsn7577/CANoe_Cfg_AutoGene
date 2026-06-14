# coTfsNmtResetNode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsNmtResetNode( void );
```

## Description

This call triggers a NMT message that resets the DUT Device Under Test. After sending out the message, the boot-up message of the DUT is awaited. The reliable wait time corresponds to the general wait time, which is set with coTfsSetTimeoutValue.

If the heartbeat producer is already active, it will be restored at the end.

## Return Values

Error code

## Example

```c
if (coTfsNmtResetNode() != 1) {
  write("reset node failed");
}
```
