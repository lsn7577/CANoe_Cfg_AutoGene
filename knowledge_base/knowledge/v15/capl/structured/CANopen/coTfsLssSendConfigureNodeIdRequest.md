# coTfsLssSendConfigureNodeIdRequest

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendConfigureNodeIdRequest( dword NID, byte[] pErrorCode, byte[] pSpecificError );
```

## Description

This function sends a configure LSS configure node-ID request and waits for the response.

## Parameters

| Name | Description |
|---|---|
| NID | node-ID of the device under test (DUT), value range 1..127 and 255 |
| pErrorCode | error code 0 - protocol successfully completed1 - node-ID out of range255 - implementation specific error occurred |
| pSpecificError | manufacturer specific error (used if error code = 255) |

## Return Values

Error code

## Example

```c
byte pErrorCode[1];
byte pSpecificError[1];

/* send LSS configure nodeID request and wait for response */

if (coTfsLssSendConfigureNodeIdRequest( 112 , pErrorCode, pSpecificError) == 1) {
  /* request sent and DUT replied with correct response. Response values can be found in pErrorCode, pSpecificError */
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
