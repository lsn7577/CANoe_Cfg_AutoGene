# coTfsActivateSyncMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsActivateSyncMonitor( dword canId, dword producerTime, dword tolerance, dword windowLength, dword maxCounter );
```

## Description

This function checks whether the DUT Device Under Test as sync producer makes the sync available within the defined times.

For each correct occurrence, the callback void coTfsOnSyncMsg (dword nodeId) is called. If the time is not adhered to, then the callback void coTfsOnSyncFail(dword nodeId, dword cause) is called. After an error has occurred, the callback system is automatically disabled. The reason for the error is specified in the parameter cause:1 = Message distance too small2 = Message distance too large or message is missing

This check can be switched off again with coTfsDeactivateSyncMonitor. Only one DUT can be monitored at a time.

The optional sync counter is checked. maxCounter contains the highest allowed number. See DS301 V4.1 for more information.

The description of coTfsActivateHeartbeatMonitor contains a temporal representation that can be applied sensibly to this function.

## Return Values

Error code

## Example

```c
coTfsActivateSyncMonitor( 0x008080, 100, 20, 10, 64);
```
