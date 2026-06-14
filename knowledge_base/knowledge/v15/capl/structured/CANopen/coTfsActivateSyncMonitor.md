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

## Parameters

| Name | Description |
|---|---|
| canID | CANopen® CAN-ID of the DUT. |
| producerTime | Sync time in micro seconds. |
| tolerance | Permitted time deviation of the target device in micro seconds. It is recommended that you use an even value. The tolerated time frame within a message is still accepted is: x - (delta/2) <= x <= x + (delta/2) |
| windowLength | Synchronous PDO window length in micro seconds. |
| maxCounter | 1 < maxCounter < 241 |

## Return Values

Error code

## Example

```c
coTfsActivateSyncMonitor( 0x008080, 100, 20, 10, 64);
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
