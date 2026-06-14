# coTfsDeactivateSyncMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsDeactivateSyncMonitor( dword canId );
```

## Description

This function switches off the calling of the sync callbacks if these are switched on. Furthermore all active sync PDO checks are also disabled.

The callbacks can be switched on with coTfsActivateSyncMonitor.

## Parameters

| Name | Description |
|---|---|
| canId | CAN identifier |

## Return Values

Error code

## Example

```c
coTfsActivateSyncMonitor(0x080080,100.20);
TestWaitForTimeout(2000);
coTfsDeactivateSyncMonitor(0x008080);
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
