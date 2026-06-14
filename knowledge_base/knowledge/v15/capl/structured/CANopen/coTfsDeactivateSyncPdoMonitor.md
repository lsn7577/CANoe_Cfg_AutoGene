# coTfsDeactivateSyncPdoMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsDeactivateSyncPdoMonitor( dword pdoCanId );
```

## Description

This function switches off the calling of all switched on sync PDO callbacks.

The callbacks can be switched on with coTfsActivateSyncPdoMonitor.

## Parameters

| Name | Description |
|---|---|
| pdoCanId | CAN-ID of the PDO to be monitored. |

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
