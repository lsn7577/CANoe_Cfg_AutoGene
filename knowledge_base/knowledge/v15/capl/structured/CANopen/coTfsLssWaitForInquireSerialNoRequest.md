# coTfsLssWaitForInquireSerialNoRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForInquireSerialNoRequest( dword serialNo );
```

## Description

This function waits for the Inquire serial number request and sends the response.

## Parameters

| Name | Description |
|---|---|
| serialNo | Serial number part of the LSS address. |

## Return Values

Error code

## Example

```c
/* waits for LSS inquire serial number request */
if (coTfsLssWaitForInquireSerialNoRequest( 0x12345678 ) == 1) {
  /* received LSS inquire serial number request, sent response with serial number */
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
