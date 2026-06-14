# coTfsNmtResetCommunication

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsNmtResetCommunication( void );
```

## Description

This call triggers a NMT message that resets the communication functionality of the DUT Device Under Test. After sending out the message, the boot-up message of the DUT is awaited. The reliable wait time corresponds to the general wait time, which is set with coTfsSetTimeoutValue.

If the heartbeat producer is already active, it will be restored at the end.

## Return Values

Error code

## Example

```c
if ( coTfsNmtResetCommunication() != 1) {
  write("reset communication failed");
}
```
