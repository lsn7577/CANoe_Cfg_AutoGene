# LINtp_PreSend

> Category: `LIN` | Type: `function`

## Syntax

```c
void LINtp_PreSend(byte data[]);
```

## Description

The callback function is called before a LIN message is sent with the provided data.

## Parameters

| Name | Description |
|---|---|
| data | Message data |

## Return Values

—

## Example

```c
Lintp_PreSend(byte data[])
{
  // ...
  // change sequence number of the consecutive frame
  data[1] = data[1] + 1;
  // ...
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | — | — | — | — |
| Restricted To | — | LIN Real bus mode | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
