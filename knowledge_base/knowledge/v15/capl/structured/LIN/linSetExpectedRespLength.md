# linSetExpectedRespLength

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetExpectedRespLength(long frameID, long numberOfBytes);
```

## Description

This function can be used to configure how many data bytes of the frame response will be expected on reception. Reception of a LIN frame with a number of data bytes deviant from the expected number of bytes will lead to either a CRC error (if more bytes were received than expected) or a RcvError (if less bytes were received than expected). The actual length of frames transmitted on the bus will remain unchanged.

To change the maximum number of bytes transmitted, use linSetRespLength. linSetRespLength and linSetExpectedRespLength cannot be used together to correctly reconfigure a LIN frame to be sent with a different length. Use output(linFrame) for this purpose.

## Parameters

| Name | Description |
|---|---|
| frameID | Identifier of the LIN frame to be configured. Value range: 0…63 |
| numberOfBytes | Number of expected data bytes (excluding the CRC byte). Value range: 1..8 |

## Return Values

On success, returns 1, otherwise 0.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 SP2 | 14 SP2 | — | — | —✔ |
| Restricted To | — | LIN | LIN | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | —✔ |
| 32-Bit | — | ✔ | ✔ | N/A | — | —✔ |
| 64-Bit | — | ✔ | ✔ | — | — | —✔ |
