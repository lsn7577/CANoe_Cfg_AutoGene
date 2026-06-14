# coTfsLssWaitForSwitchStateSelectiveSequence

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForSwitchStateSelectiveSequence( dword[] pVendorId, dword[] pProductCode, dword[] pRevisionNo, dword[] pSerialNo );
```

## Description

The function waits for a switch state selective messages and sends the response. For a successful test all parameters are to be received within a defined time-out.

## Parameters

| Name | Description |
|---|---|
| pVendorId | Vendor-ID part of the LSS address. |
| pProductCode | Product code part of the LSS address. |
| pRevisionNo | Revision number part of the LSS address. |
| pSerialNo | Serial number part of the LSS address. |

## Return Values

Error code

## Example

```c
dword pVendorId[1];
dword pProductCode[1];
dword pRevisionNo[1];
dword pSerialNo[1];

/* waits for LSS switch state selective request */
if (coTfsLssWaitForSwitchStateSelectiveSequence( pVendorId, pProductCode, pRevisionNo, pSerialNo) == 1) {
  /* received LSS switch state selective request */
  /* received values can be found in pVendorId[0], pProductCode[0], pRevisionNo[0], pSerialNo[0] */
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
