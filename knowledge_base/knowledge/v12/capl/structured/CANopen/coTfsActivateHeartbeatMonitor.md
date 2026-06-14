# coTfsActivateHeartbeatMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsActivateHeartbeatMonitor( dword nodeID, dword producerTime, dword tolerance );
```

## Description

This function checks whether the DUT Device Under Test as heartbeat producer makes the heartbeat message available within the defined times.

For each correct occurrence, the callback void coTfsOnHeartbeatMsg (dword nodeId) is called. If the time is not adhered to, then the callback void coTfsOnHeartbeatFail(dword nodeId, dword cause) is called. After an error has occurred, the callback system is automatically disabled. The reason for the error is specified in the parameter cause:1 = Message distance too small2 = Message distance too large or message is missing

Only one DUT can be monitored at a time. This check can be switched off again with coTfsDeactivateHeartbeatMonitor.

## Return Values

Error code

## Example

Demonstration of the mode of operation of coTfsActivateHeartbeatMonitor and the corresponding callback functions

```c
coTfsActivateHeartbeatMonitor (0x1, 100, 20);
```
