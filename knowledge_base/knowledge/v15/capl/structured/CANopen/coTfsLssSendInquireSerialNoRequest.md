# coTfsLssSendInquireSerialNoRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendInquireSerialNoRequest( dword[] pSerialNo );
```

## Description

This function sends an Inquire serial number request and waits for the response.

## Parameters

| Name | Description |
|---|---|
| pSerialNo | Serial number part of the LSS address. |

## Return Values

Error code

## Example

```c
dword pSerialNo[1];

/* send LSS inquire serial number request */

if (coTfsLssSendInquireSerialNoRequest( pSerialNo ) == 1) {
  /* sent LSS inquire serial number request and received response */
  /* received value can be found in pSerialNo */
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
