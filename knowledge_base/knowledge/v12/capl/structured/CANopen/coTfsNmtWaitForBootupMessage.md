# coTfsNmtWaitForBootupMessage

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsNmtWaitForBootupMessage( void ):
```

## Description

This function waits for the boot-up message.

If the heartbeat producer is already active, it will be restored at the end.

## Return Values

Error code

## Example

```c
/* wait for a bootup message */
if (coTfsNmtWaitForBootupMessage() == 1) {
  write("Bootup message received");
}
```
