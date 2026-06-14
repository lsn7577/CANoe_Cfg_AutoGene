# KLine_SetUARTParameter

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetUARTParameter(dword dataBits, dword parity, dword stopBits);
```

## Description

Configures the way bytes are sent on K-Line, by setting the parameters the UART (universal asynchronous receiver/transmitter) uses.

## Parameters

| Name | Description |
|---|---|
| dataBits | Number of bits a byte consists of.Possible values: 7, 8, 9.Note: 7 bits in a byte will not allow standard K-Line communication. |
| parity | If a parity bit is used to indicate the number of bits set in the byte 1 means _odd_ and 2_even_ parity.A value of 0 indicates that no parity bit is used. |
| stopBits | The number of stop bits that indicate the end of a byte. 1 or 2 is possible. |

## Return Values

On success 0, otherwise error code.

## Example

```c
KLine_CreateECURepresentation( gMsgChannel);
KLine_SetUARTParameter( 9, 1, 2); // 9 data bits, odd parity, 2 stop bits => 13 bit/byte (including start bit)
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 | 9.0 | — | — | — | 2.1 |
| Restricted To | K-Line Real bus mode | K-Line Real bus mode | — | — | — | K-Line Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
