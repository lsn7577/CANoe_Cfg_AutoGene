# coTfsLssAddMasterResponseConfigureBitTiming

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssAddMasterResponseConfigureBitTiming( dword tableSelector, dword tableSelectorMask, dword tableIndex, dword tableIndexMask, dword errCode, dword specError );
```

## Description

This function adds a single LSS Master request wait condition to the internal list of LSS Master request wait conditions and sends a response if a request is received.

## Parameters

| Name | Description |
|---|---|
| tableSelector | Selects which bit timing parameter table shall be used. 0 - standard CiA® CiA® is a registered community trade mark of CAN in Automation e.V. bit timing table1..127 - reserved128..255 - may be used for manufacturer specific bit timings |
| tableSelectorMask | Mask for table selector; set bits are compared, not set bits are not compared. |
| tableIndex | CAN bitrate index. 0 = 1 MBit/s1 = 800 kBit/s2 = 500 kBit/s3 = 250 kBit/s4 = 125 kBit/s5 = 100 kBit/s (reserved value, do not use)6 = 50 kBit/s7 = 20 kBit/s8 = 10 kBit/s |
| tableIndexMask | Mask for table index; set bits are compared, not set bits are not compared. |
| errCode | Error code. 0 - protocol successfully completed1 - bit timing not supported255 - implementation specific error occurred |
| specError | Manufacturer specific error (used if error code = 255). |

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
if (coTfsLssAddMasterResponseConfigureBitTiming( ) {
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
