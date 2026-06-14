# coTfsNmtStartNode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsNmtStartNode( void );
```

## Description

This call triggers a NMT message that sets the DUT Device Under Test into the operational state. The set state is checked with heartbeat and guarding mechanisms.

For this, there is first an attempt to configure a heartbeat producer in the DUT (object 0x1017). The heartbeat message contains the current device status. If the DUT should not make a heartbeat producer available, a remote guarding frame is sent to the DUT. The DUT responds with the corresponding guarding response. The procedure is repeated again. The second response is evaluated and contains the device status. The CANopen® specification provides that a CANopen® device supports at least one of the two modes.

If the heartbeat producer is already active, it will be restored at the end.

## Return Values

Error code

## Example

```c
if ( coTfsNmtStartNode() != 1) {
  write("start node failed");
}
```
