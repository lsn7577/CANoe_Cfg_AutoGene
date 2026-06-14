# getPayloadData

> Category: `CAN` | Type: `function`

## Syntax

```c
getPayloadData(errorframe errFrame, byte[] payload, dword payloadSize;
```

## Description

Returns the valid payload of a frame that was interrupted during transmission.

Depending on error position valid bits are written to the payload parameter. If there is no payload data, nothing is written into the payload parameter.

## Parameters

| Name | Description |
|---|---|
| errFrame | Error frame which includes the payload. |
| payload | Array for writing the transmitted payload of the error frame. |
| payloadSize | Size of the payload parameter. |

## Example

```c
variables
{
  byte payload[64];
  dword validBits;
}

on errorFrame
{
  int i = 0;
  byte validPayload[64];

  validBits = getPayloadData(this, validPayload, elcount(validPayload));
  byteCount = validBits / 8;
  bitCount = validBits % 8;

  dataLength =  dlcToDataLength[this.DLC];

  for(i = 0; i < byteCount; ++i)
  {
    payload[i] = this.byte(i);
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 14 SP2 | 14 SP2 | 14 SP2 | 14 SP2 | — | 6 |
| Restricted To | CAN | CAN | CAN | CAN | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | ✔ | — | N/A |
