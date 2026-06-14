# coTfsLssSendSwitchStateSelectiveSequence

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendSwitchStateSelectiveSequence( dword vendorId, dword productCode, dword revisionNo, dword serialNo );
```

## Description

The function sends a switch state selective messages and waits for the response.

## Parameters

| Name | Description |
|---|---|
| vendorId | Vendor-ID part of the LSS address. |
| productCode | Product code part of the LSS address. |
| revisionNo | Revision number part of the LSS address. |
| serialNo | Serial number part of the LSS address. |

## Return Values

Error code

## Example

```c
/* send LSS switch state selective protocol request */

if (coTfsLssSendSwitchStateSelectiveSequence( 0x12345678,  0x11223344, 0x87654321, 0x1) != 1) {
  /* message could not be sent */
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
