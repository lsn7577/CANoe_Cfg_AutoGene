# linUpdateResponse

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linUpdateResponse(dword frameId, dword dlc, byte[] responseData); // form 1
dword linUpdateResponse(linFrame frame); // form 2
```

## Description

Updates the response data of a specific LIN frame.

## Parameters

| Name | Description |
|---|---|
| frameId | ID of the LIN frame whose response will be updated. Value range: 0..63 |
| dlc | Number of data bytes contained in the frame (Data Length Code). Value range: 0..8 |
| responseData | An array of bytes which contains the response data to be set. |
| frame | The LIN frame whose response will be updated. |

## Return Values

Returns 1 if the response update succeeded, otherwise 0.

## Example

```c
// Update the response of the LIN frame with the id 0x04

on linFrame 0x04

{
  long i;
  byte frm4data[8];

  for(i = 0; i < linGetDlc(this.id); i++)
  {
    frm4data[i] = this.byte(i) + 1;
  }

linUpdateResponse(this.id, linGetDlc(this.id), frm4data);
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
