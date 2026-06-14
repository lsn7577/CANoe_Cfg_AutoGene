# coTfsLssSetMasterResponseIdentifyRemoteSlaveMask

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSetMasterResponseIdentifyRemoteSlaveMask( dword vendorIdMask, dword productCodeMask, dword revisionNoLowMask, dword revisionNoHighMask, dword serialNoLowMask, dword serialNoHighMask );
```

## Description

This function sets the masks for the parameters of function coTfsLssAddMasterResponseIdentifyRemoteSlave and has to be called before that function.

## Parameters

| Name | Description |
|---|---|
| vendorIdMask | Mask for vendor-ID parameter; set bits are compared, not set bits are not compared. |
| productCodeMask | Mask for product code parameter; set bits are compared, not set bits are not compared. |
| revisionNoLowMask | Mask for low boundary of revision number parameter; set bits are compared, not set bits are not compared. |
| revisionNoHighMask | Mask for high boundary of revision number parameter; set bits are compared, not set bits are not compared. |
| serialNoLowMask | Mask for low boundary of serial number parameter; set bits are compared, not set bits are not compared. |
| serialNoHighMask | Mask for high boundary of serial number parameter; set bits are compared, not set bits are not compared. |

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
