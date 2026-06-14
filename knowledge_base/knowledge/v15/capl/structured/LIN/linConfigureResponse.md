# linConfigureResponse

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linConfigureResponse(dword frameId, dword dlc, byte[] responseData); // form 1
dword linConfigureResponse(linFrame frame); // form 2
```

## Description

Configures a response frame of a LIN node if no database is used.

## Parameters

| Name | Description |
|---|---|
| frameId | ID of the LIN frame which will be configured as response. Value range: 0..63 |
| dlc | Number of data bytes contained in the frame (Data Length Code). Value range: 0..8 |
| responseData | An array of bytes which contains the response data to be set. |
| frame | The LIN frame which will be configured as response. |

## Return Values

Returns 1 if the configuration of the response succeeded, otherwise 0.

## Example

```c
// Configure the LIN frame with the ID 0x01 as response of the slave and initialize the value of all response bytes to zero.

on preStart

{
  long i;
  byte responseData [8];

  for(i = 0; i < 8; i++)
  {
    responseData [i] = 0;
  }

  linConfigureResponse(0x01, 8, responseData);
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
