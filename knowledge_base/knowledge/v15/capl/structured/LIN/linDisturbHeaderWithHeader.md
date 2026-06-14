# linDisturbHeaderWithHeader

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linDisturbHeaderWithHeader(dword byteIndex, dword bitIndex, long disturbingFrameId);
```

## Description

Configures the LIN hardware to disturb the next header with a new header (id=<disturbanceHeaderID>).

## Parameters

| Name | Description |
|---|---|
| byteIndex | Starts disturbance in byte with index <byteIndex>. 0: Sync Byte 1: ProtectedId Byte |
| bitIndex | Starts disturbance at bit position <bitIndex>. An index in the range 0-7 specifies a data bit, while the index 8 specifies the stop bit. Higher index values specify the interbyte-space after the indexed data byte. In which case, the user should make sure that the interbyte space is large enough. Value range: 0..255 |
| Note This is not the ID of the header to be disturbed, but the ID of the header disturbance itself. |  |

## Return Values

On success, a value unequal to zero, otherwise zero.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.5 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
