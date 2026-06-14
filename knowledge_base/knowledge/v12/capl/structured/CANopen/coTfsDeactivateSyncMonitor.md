# coTfsDeactivateSyncMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsDeactivateSyncMonitor( dword canId );
```

## Description

This function switches off the calling of the sync callbacks if these are switched on. Furthermore all active sync PDO checks are also disabled.

The callbacks can be switched on with coTfsActivateSyncMonitor.

## Return Values

Error code

## Example

```c
coTfsActivateSyncMonitor(0x080080,100.20);
TestWaitForTimeout(2000);
coTfsDeactivateSyncMonitor(0x008080);
```
