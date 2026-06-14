# coTfsLssAddMasterResponseIdentifyRemoteSlave

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssAddMasterResponseIdentifyRemoteSlave( dword vendorId, dword productCode, dword revisionNoLow, dword revisionNoHigh, dword serialNoLow, dword serialNoHigh );
```

## Description

This function adds a single LSS Master request wait condition to the internal list of LSS Master request wait conditions and sends a response if a request is received.

## Parameters

| Name | Description |
|---|---|
| vendorId | Vendor-ID |
| productCode | Product code |
| revisionNoLow | Low boundary of the revision number. |
| revisionNoHigh | High boundary of the revision number. |
| serialNoLow | Low boundary of the serial number. |
| serialNoHigh | High boundary of the serial number. |

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

if (coTfsLssSetMasterResponseIdentifyRemoteSlaveMask( 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF ) {
  if (coTfsLssAddMasterResponseIdentifyRemoteSlave( 0x1234, 0x43214321, 0, 0xFFFFFFFF, 0, 1000 ) {
    write("could not add request");
    return;
  }
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
