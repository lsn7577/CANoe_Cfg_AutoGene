# ScanBaudrateActive

> Category: `CAN` | Type: `function`

## Syntax

```c
long ScanBaudrateActive( dword channel, dword messageID, double firstBaudrate, double lastBaudrate, dword timeout);
```

## Description

The function determines the baud rate for the given channel. Result of the function is written into the Write Window.

The baud rate scanner checks different baud rates and tries to send a message through the given channel. The function is finished if the message was sent successfully and the baud rate was determined. If a wrong baud rate is present, the other power supply takers cannot receive the message. CANoe as the transmitter does not receive an acknowledge and sends an Error Frame. In this case the next baud rate of the baud rate range is checked.

## Parameters

| Name | Description |
|---|---|
| channel | Channel number. (1,..,32) |
| messageID | ID of the message that the scanner will send to detect the baud rate. The DLC of the message is always 8. |
| firstBaudrate / lastBaudrate | Baud rate range to scan. If both values are set to zero the scanner checks the most commonly used baud rates:33.333, 50.0, 83.333, 100.0, 125.0, 250.0, 500.0, 1000.0 [kBaud] If both values are the same but not zero the scanner multiplies the baud rate with a given factor (Value range 0.25-5.0). The factor is changed with steps of 0.25. If both values are different, all possible baud rate values in the ranged are scanned.The incremental step in the range is 1.5%. |
| timeout | Period of time [ms] the scanner waits when the message is sent. |

## Return Values

Returns 0 if the scan function was successfully started. Otherwise the return value is non-zero.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.1 | 5.1 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
