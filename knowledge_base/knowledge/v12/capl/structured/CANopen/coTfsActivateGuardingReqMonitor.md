# coTfsActivateGuardingReqMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsActivateGuardingReqMonitor( dword nodeID, dword guardTime, dword tolerance );
```

## Description

When this function is called, it is checked whether the DUT Device Under Test makes available the remote frame for the guarding within the defined times.

For each correct occurrence, the callback void coTfsOnGuardingRTRMsg(dword nodeId) is called. If the time is not adhered to, then the callback void coTfsOnGuardingRTRFail(dword nodeId, dword cause) is called once. After an error has occurred, the callback system is automatically disabled. The reason for the error is specified in the parameter cause:1 = Message distance too small2 = Message distance too large or message is missing

This check can be switched off again with coTfsDeactivateGuardingReqMonitor. Only one DUT can be monitored at a time.

The description of coTfsActivateHeartbeatMonitor contains a temporal representation that can be applied sensibly to this function.

## Return Values

Error code

## Example

```c
coTfsActivateGuardingReqMonitor( 0x1, 100, 20 );
```
