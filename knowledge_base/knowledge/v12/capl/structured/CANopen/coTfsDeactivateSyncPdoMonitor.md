# coTfsDeactivateSyncPdoMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsDeactivateSyncPdoMonitor( dword pdoCanId );
```

## Description

This function switches off the calling of all switched on sync PDO callbacks.

The callbacks can be switched on with coTfsActivateSyncPdoMonitor.

## Return Values

Error code

## Example

```c
coTfsActivateSyncMonitor(0x80, 1000000, 500000, 50000); // 1s, 500 ms, 50 ms
entryNb[0] = coTfsActivateSyncPDOMonitor(0x181);
entryNb[1] = coTfsActivateSyncPDOMonitor(0x182);
entryNb[2] = coTfsActivateSyncPDOMonitor(0x183);

// ... callbacks are active ...
coTfsDeactivateSyncPdoMonitor(0x008080); // disables all sync pdo callbacks
coTfsDeactivateSyncMonitor(); // disable sync check
```
