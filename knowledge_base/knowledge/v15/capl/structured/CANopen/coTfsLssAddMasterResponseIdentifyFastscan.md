# coTfsLssAddMasterResponseIdentifyFastscan

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssAddMasterResponseIdentifyFastscan( dword idNumber, dword idNumberMask, dword bitCheck, dword bitCheckMask, dword sub, dword subMask, dword next, dword nextMask );
```

## Description

This function adds a single LSS Master request wait condition to the internal list of LSS Master request wait conditions and sends a response if a request is received.

## Parameters

| Name | Description |
|---|---|
| idNumber | FastScan ID |
| idNumberMask | Mask for FastScan ID; set bits are compared, not set bits are not compared. |
| bitCheck | FastScan bitcheck value, used to define the used bitmask for LSS FastScan. |
| bitCheckMask | Bitmask for LSS FastScan; set bits are compared, not set bits are not compared. |
| sub | FastScan sub, defines which part of the LSS-ID is transmitted in idNumber 0 - vendor-ID1 - product code2 - revision number3 - serial number |
| subMask | Mask for FastScan sub; set bits are compared, not set bits are not compared. |
| next | FastScan next, specifies the sub for the next request. |
| nextMask | Mask for FastScan next; set bits are compared, not set bits are not compared. |

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
if (coTfsLssAddMasterResponseIdentifyFastscan( 0x000002, 0xFFFFFFFF, 28, 0xFFFFFFFF, 1, 0xFFFFFFFF, 1, 0xFFFFFFFF) {
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
