# linIsBitStreamBusy

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linIsBitStreamBusy(); // form 1
dword linIsBitStreamBusy(dword channel); // form 2
```

## Description

Queries the current LIN bit stream sending status.

## Parameters

| Name | Description |
|---|---|
| channel | The LIN channel number which will be queried. |

## Return Values

Returns 1 if a bit stream is currently being sent, otherwise 0.

## Example

```c
// Make sure that there is no bit stream sending active before a new transmission is started

if (linIsBitStreamBusy() == 0)

{
  linSendBitStream(data, numberOfBits);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 10.0 | — | — | — | 2.2 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
