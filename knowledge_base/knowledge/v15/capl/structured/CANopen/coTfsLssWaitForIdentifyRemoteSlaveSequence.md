# coTfsLssWaitForIdentifyRemoteSlaveSequence

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForIdentifyRemoteSlaveSequence( dword[] pVendorId, dword[] pProductCode, dword[] pRevNoLowBound, dword[] pRevNoHighBound, dword[] pSerialNoLowBound, dword[] pSerialNoHighBound );
```

## Description

This function waits for a LSS identify remote slave sequence.

For a successful test all parameters are to be received within a defined time-out.

## Parameters

| Name | Description |
|---|---|
| pVendorId | Vendor-ID |
| pProductCode | Product code |
| pRevNoLowBound | Low boundary of the revision number. |
| pRevNoHighBound | High boundary of the revision number. |
| pSerialNoLowBound | Low boundary of the serial number. |
| pSerialNoHighBound | High boundary of the serial number. |

## Return Values

Error code

## Example

```c
dword pVendorId[1];
dword pProductCode[1];
dword pRevNoLowBound[1];
dword pRevNoHighBound[1];
dword pSerialNoLowBound[1];
dword pSerialNoHighBound[1];

/* waits for a LSS identify remote slave sequence */
if (coTfsLssWaitForIdentifyRemoteSlaveSequence( pVendorId, pProductCode, pRevNoLowBound, pRevNoHighBound, pSerialNoLowBound,pSerialNoHighBound ) == 1) {
  /* waits for LSS identify remote slave sequence */
  /* received values can be found in pVendorId, pProductCode, pRevNoLowBound, pRevNoHighBound, pSerialNoLowBound,pSerialNoHighBound */
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
