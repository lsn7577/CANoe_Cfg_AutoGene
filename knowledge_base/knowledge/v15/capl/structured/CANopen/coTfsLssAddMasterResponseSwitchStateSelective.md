# coTfsLssAddMasterResponseSwitchStateSelective

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssAddMasterResponseSwitchStateSelective( dword vendorId, dword vendorIdMask, dword productCode, dword productCodeMask, dword revNo, dword revNoMask, dword serialNo, dword serialNoMask );
```

## Description

This function adds a single LSS Master request wait condition to the internal list of LSS Master request wait conditions and sends a response if a request is received.

## Parameters

| Name | Description |
|---|---|
| vendorId | Vendor-ID part of the LSS address. |
| vendorIdMask | Mask for vendor-ID part of the LSS address; set bits are compared, not set bits are not compared. |
| productCode | Product code part of the LSS address. |
| productCodeMask | Mask for product code part of the LSS address; set bits are compared, not set bits are not compared. |
| revNo | Revision number part of the LSS address. |
| revNoMask | Mask for revision number part of the LSS address; set bits are compared, not set bits are not compared. |
| serialNo | Serial number part of the LSS address. |
| serialNoMask | Mask for serial number part of the LSS address; set bits are compared, not set bits are not compared. |

## Return Values

Error code

## Example

```c
/* clear internal check list */
if (coTfsLssClearMasterResponseList() != 1) {
  write("Clear list failed");
  return;
} 

/* add one or more test functions */
if (coTfsLssAddMasterResponseSwitchStateSelective( 0x12341234, 0xFFFFFFFF, 0, 0, 0x0001, 0xFFFFFFFF, 0, 0 ) {
  write("could not add request");
  return;
} 

/* wait for any of the events configured before */
if (coTfsLssWaitForMasterRequestMessage() != 1) {
  write("no event received");
} 
else {
  write("event received");
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
