# RS232SetHandshake

> Category: `RS232` | Type: `function`

## Syntax

```c
dword RS232SetHandshake( dword port, dword handshake, dword XonLimit, dword XoffLimit, dword XonChar, dword XoffChar );
dword RS232SetHandshake( dword port, dword handshake, dword XonLimit, dword XoffLimit, dword XonChar, dword XoffChar, dword timeout ); // deprecated
```

## Description

Sets handshake parameters on serial port.

## Parameters

| Name | Description |
|---|---|
| port | A number between 1 and 255 identifying a serial port. |
| 0 | no handshake at all |
| 10 | hardware handshake, use DTR<->DSR |
| 33 | hardware handshake, use RTS<->CTS |
| 65 | hardware handshake, use RTS<->CTS, use “toggle” variant |
| 128 | software handshake, use Xon and Xoff characters |
| Note Mixtures of hardware and software handshake are not supported. For sake of compatibility, it is possible to set signal lines to fixed levels with this function. Please prefer for that purpose RS232SetSignalLine. |  |
| XonLimit | Parameter for software flow control. Specifies the minimum number of bytes allowed in the input buffer before the XonChar is sent. |
| Note XonLimit and XoffLimit must be set properly to prevent errors, i.e. XonLimit < (input buffer size – XoffLimit) must apply. |  |
| XonChar | Parameter for software flow control. It specifies the value of the XON character to start an operation (transmission as well as reception). |
| Note The transmitted data must not contain the XON and XOFF characters if software flow control is used. XON and XOFF are sent only once for each transition. |  |
| -1 | infinite |
| <10 | not allowed |
| Note A timeout should not be used as it might stop a transmission that is not completed. |  |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1 | 7.1 | — | — | 14 | 2.1 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | — | — | ✔ | N/A |
