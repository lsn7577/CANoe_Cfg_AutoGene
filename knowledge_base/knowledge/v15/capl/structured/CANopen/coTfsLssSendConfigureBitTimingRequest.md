# coTfsLssSendConfigureBitTimingRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendConfigureBitTimingRequest( dword tableSelector, dword tableIndex, byte[] pErrorCode, byte[] pSpecificError );
```

## Description

This function sends a LSS Configure Bit-Timings Parameters request and waits for the response.

## Parameters

| Name | Description |
|---|---|
| tableSelector | Selects which bit timing parameter table shall be used. 0 - standard CiA® CiA® is a registered community trade mark of CAN in Automation e.V. bit timing table1..127 - reserved128..255 - may be used for manufacturer specific bit timings |
| tableIndex | CAN bitrate index. 0 = 1 MBit/s1 = 800 kBit/s2 = 500 kBit/s3 = 250 kBit/s4 = 125 kBit/s5 = 100 kBit/s (reserved value, do not use)6 = 50 kBit/s7 = 20 kBit/s8 = 10 kBit/s |
| pErrorCode | Error code. 0 - protocol successfully completed1 - bit timing not supported255 - implementation specific error occurred |
| pSpecificError | Manufacturer specific error (used if error code = 255). |

## Return Values

Error code

## Example

```c
byte pErrorCode[1];
byte pSpecificError[1];

/* send LSS configure bit timing request and wait for reponse*/

if (coTfsLssSendConfigureBitTimingRequest( 0, 3, pErrorCode, pSpecificError) == 1) {
  /* request sent with parameters tableSelector=0 and tableIndex=3 and DUT replied with correct response. Response values can be found in pErrorCode, pSpecificError */
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
