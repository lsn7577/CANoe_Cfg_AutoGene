# coTfsLssSendFastScanRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendFastScanRequest( dword idNumber, dword bitCheck, dword sub, dword next );
```

## Description

This function sends a LSS fast scan protocol request.

## Parameters

| Name | Description |
|---|---|
| idNumber | FastScan ID |
| bitCheck | FastScan bitcheck value, used to define the used bitmask for LSS FastScan. |
| sub | FastScan sub, defines which part of the LSS-ID is transmitted in idNumber. 0 - vendor-ID1 - product code2 - revision number3 - serial number |
| next | FastScan next, specifies the sub for the next request. |

## Return Values

Error code

## Example

```c
/* send LSS fast scan protocol request */

if (coTfsLssSendFastScanRequest(0x000002, 28, 1, 1) == 1) {
  /* request sent */
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
