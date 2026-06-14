# coTfsDeactivateGuardingReqMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsDeactivateGuardingReqMonitor( dword nodeId );
```

## Description

This function switches off the calling of the RTR callbacks if these are switched on.

The callbacks can be switched on with coTfsActivateGuardingReqMonitor.

## Return Values

Error code

## Example

```c
coTfsActivateGuardingReqMonitor(2,100,20);
TestWaitForTimeout(2000);
coTfsDeactivateGuardingReqMonitor(0x1);
```
