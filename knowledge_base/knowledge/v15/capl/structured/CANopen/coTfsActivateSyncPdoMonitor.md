# coTfsActivateSyncPdoMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsActivateSyncPdoMonitor( dword syncCanId, dword pdoCanId, dword transmissionType );
```

## Description

This function checks if the DUT Device Under Test sends a synchronous PDO with the given CAN-ID. The check is only available if the sync check was activated with coTfsActivateSyncMonitor.

For each correct occurrence, the callback void coTfsOnSyncPdoMsg(dword canId) is called. The synchronous PDO must occur in the defined time slot. If the time is not adhered to, then the callback void coTfsOnSyncPdoFail(dword canId) is called once. After an error has occurred, the callback system is automatically disabled.

This check can be switched off again with coTfsDeactivateSyncPdoMonitor.

## Parameters

| Name | Description |
|---|---|
| syncCanId | Sync CAN-ID to be used. |
| pdoCanId | CAN-ID of the PDO to be monitored. |
| transmissionType | PDO transmission type, range 1..240. |

## Return Values

Error code

## Example

```c
coTfsActivateSyncMonitor(0x80, 1000000, 500000, 50000); // 1s, 500 ms, 50 ms
coTfsActivateSyncPdoMonitor(0x181);
coTfsActivateSyncPdoMonitor(0x182);
coTfsActivateSyncPdoMonitor(0x183);

// ... callbacks are active ...
coTfsDeactivateSyncPDOMonitor(0x181); // disables one sync pdo callback

// ... others are still active ...
coTfsDeactivateSyncPDOMonitor(); // remove all checks
coTfsDeactivateSyncMonitor(); // disable sync check
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
