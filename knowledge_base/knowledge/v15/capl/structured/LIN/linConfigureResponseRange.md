# linConfigureResponseRange

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linConfigureResponseRange(byte[] frameIds, byte[] dlcs, byte[][8] responseData)
```

## Description

Configures a range of frames as response of a LIN node if no database is used.

## Parameters

| Name | Description |
|---|---|
| frameIds | Array which contains the ids of every frame to be configured. Valid frame id range: 0..63 |
| dlcs | Array of dlcs (Data Length Codes) which defines the number of data bytes for every frame to be configured. Valid dlc range: 0..8 |
| responseData | An array which points to an array of 8 bytes which contains the initial response data to be set for every frame. |

## Return Values

Returns 1 if the configuration of all given frames succeeded, otherwise 0.

## Example

```c
// Configure two LIN frames with the IDs 0x01 and 0x02 as response of the slave. The first frame contains 5 and the second one 2 data bytes.

on preStart
{
  byte ids[2] = { 0x01, 0x02 };
  byte dlcs[2] = { 5, 2 };
  byte responseData[2][8];

  responseData[0][0] =  0x55;
  responseData[0][1] =  0x55;
  responseData[0][2] =  0x55;
  responseData[0][3] =  0x55;
  responseData[0][4] =  0x55;

  responseData[1][0] =  0xAA;
  responseData[1][1] =  0xAA;

  linConfigureResponseRange(ids, dlcs, responseData);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | 13.0 | 13.0 | — | 2.2 |
| Restricted To | LIN | LIN | LIN | LIN | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
