# coTfsLssSendInquireVendorIdRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendInquireVendorIdRequest( dword[] pVendorId );
```

## Description

The function sends an Inquire vendor-ID request and waits for the response.

## Parameters

| Name | Description |
|---|---|
| pVendorId | Vendor-ID part of the LSS address. |

## Return Values

Error code

## Example

```c
dword pVendorId[1];

/* send LSS inquire vendor ID request */

if (coTfsLssSendInquireVendorIdRequest( pVendorId ) == 1) {
  /* sent LSS inquire vendor ID request and received response */
  /* received value can be found in pVendorId[0] */
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
