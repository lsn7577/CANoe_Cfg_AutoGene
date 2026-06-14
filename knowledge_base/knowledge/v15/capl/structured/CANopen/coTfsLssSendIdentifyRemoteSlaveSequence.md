# coTfsLssSendIdentifyRemoteSlaveSequence

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendIdentifyRemoteSlaveSequence( dword vendorId, dword productCode, dword revNoLowBound, dword revNoHighBound, dword serialNoLowBound, dword serialNoHighBound );
```

## Description

This function sends a LSS identify remote slave sequence.

## Parameters

| Name | Description |
|---|---|
| vendorId | Vendor-ID |
| productCode | Product code |
| revNoLowBound | Low boundary of the revision number. |
| revNoHighBound | High boundary of the revision number. |
| serialNoLowBound | Low boundary of the serial number. |
| serialNoHighBound | High boundary of the serial number. |

## Return Values

Error code

## Example

```c
/* sends LSS identify remote slave sequence */

if (coTfsLssSendIdentifyRemoteSlaveSequence( 0x1234, 0x43214321, 0, 0xFFFFFFFF, 0, 1000 ) == 1) {
  /* received LSS identify remote slave sequence, sent response with selected parameters */
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
