# mostStringToAscii

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostStringToAscii(byte sourceData[], long sourceDatalen, char buffer[], long buffersize);
```

## Description

Convert MOST string to ASCII string. Unsupported characters in the input data are ignored.

## Parameters

| Name | Description |
|---|---|
| sourceData | A buffer containing the MOST string to be decoded. |
| sourceDataLen | The size of the buffer containing the MOST string. |
| buffer | Buffer to which the ASCII string is copied. |
| bufferSize | Maximum number of copied ASCII string bytes (can be specified with (elcount(buffer))). |

## Example

Output:

ASCII: abc

```c
byte data[9] = {0x00,0x00,0x61,0x00,0x62,0x00,0x63,0x00,0x00);
char buffer[200];
if(0 < mostStringToAscii(data, elcount(data), buffer, elcount(buffer)))
  write("ASCII: %s", buffer);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 | 7.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
