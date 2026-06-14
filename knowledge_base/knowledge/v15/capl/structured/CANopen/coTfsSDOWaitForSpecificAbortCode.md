# coTfsSDOWaitForSpecificAbortCode

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsSDOWaitForSpecificAbortCode( dword nodeId, dword sdoAbortCode );
```

## Description

The function waits for receiving the specified SDO abort message of the device or the occurrence of a time-out.

## Parameters

| Name | Description |
|---|---|
| nodeId | Node-ID of the device, 1..127. |
| sdoAbortCode | SDO abort code. |

## Return Values

Error code

## Example

```c
dword nodeId = 0x5;

if (coTfsSDOWaitForSpecificAbortCode(nodeId, sdoAbortCode) == 1) {
  write("SDO abort message received");
}
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
