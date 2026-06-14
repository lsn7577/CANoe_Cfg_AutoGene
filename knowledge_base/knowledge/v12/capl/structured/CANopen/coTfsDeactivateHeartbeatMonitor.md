# coTfsDeactivateHeartbeatMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsDeactivateHeartbeatMonitor( dword nodeId );
```

## Description

This function switches off the calling of the heartbeat callbacks if these are switched on.

The callbacks can be switched on with coTfsActivateHeartbeatMonitor.

## Return Values

Error code

## Example

```c
coTfsActivateHeartbeatMonitor(0x1,100.20);
TestWaitForTimeout(2000);
coTfsDeactivateHeartbeatMonitor(0x1);
```
