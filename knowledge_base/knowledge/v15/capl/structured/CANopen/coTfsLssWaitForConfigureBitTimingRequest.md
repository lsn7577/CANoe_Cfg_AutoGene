# coTfsLssWaitForConfigureBitTimingRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForConfigureBitTimingRequest( byte[] pTableSelector, byte[] pTableIndex );
```

## Description

This function waits for LSS Configure Bit-Timings Parameters request.

## Parameters

| Name | Description |
|---|---|
| pTableSelector | Selects which bit timing parameter table shall be used. 0 - standard CiA® CiA® is a registered community trade mark of CAN in Automation e.V. bit timing table1..127 - reserved128..255 - may be used for manufacturer specific bit timings |
| pTableIndex | CAN bitrate index. 0 = 1 MBit/s1 = 800 kBit/s2 = 500 kBit/s3 = 250 kBit/s4 = 125 kBit/s5 = 100 kBit/s (reserved value, do not use)6 = 50 kBit/s7 = 20 kBit/s8 = 10 kBit/s |

## Return Values

Error code

## Example

```c
byte pTableSelector[1];
byte pTableIndex[1];

/* waits for LSS configure bit timing request */
if (coTfsLssWaitForConfigureBitTimingRequest( pTableSelector, pTableIndex) == 1) {
  /* received LSS configure bit timing request */
  /* received values can be found in pTableSelector[0], pTableIndex[0] */
}
else {
  /* no request received */
  return;
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
