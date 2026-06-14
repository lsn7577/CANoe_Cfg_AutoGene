# RS232Configure

> Category: `RS232` | Type: `function`

## Syntax

```c
dword RS232Configure( dword port, dword baudrate, dword numberOfDataBits, dword numberOfStopBits, dword parity ); // form 1
dword RS232Configure( dword port, dword baudrate, dword numberOfDataBits, dword numberOfStopBits, dword parity, dword enableParityCheck); // form 2
```

## Description

Configures a serial port.

Without setting up a configuration explicitly, the default configuration is used.

Default baud rate: 9600, 8 data bits, 1 stop bit, no parity.

If a deprecated INI file exists, the data of the INI file will be used.

With form 2 of this function you can configure a serial port to use parity without letting the operating system verify parity correctness. This form should only be used if the communication to a device was not possible when using parity and form 1 of this function.

## Parameters

| Name | Description |
|---|---|
| port | A number between 1 and 255 identifying a serial port. |
| baudrate | The symbol rate to use for reception and transmission. Typically, 9600 is used. There is a list of possible values which depends on the serial port. Normally, 115.200 is the allowed maximum. |
| numberOfDataBits | The number of data bits within a transmission frame. 8 is used at most. Only values between 5 and 8 are possible. Not all values and not all combinations with other frame parameters may be supported by the serial port. |
| 1 | 1 stop bit is used ( 1 has changed meaning compared to deprecated variant RS232SetCommState ) |
| 2 | 2 stop bits are used |
| Note 1.5 stop bits are not supported any more. |  |
| 0 | no parity used, i.e. frame contains no parity bit |
| 1 | odd parity |
| 2 | even parity |
| 0 | parity verification disabled |
| !=0 (≠0) | parity verification enabled |

## Example

```c
if ( 0!=RS232Configure(1,9600,8,1,0) )
   write(“Set typical default at port 1.”);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.1/8.0 SP2: form 2 | 7.1/8.0 SP2: form 2 | — | — | 14 | 2.1 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | — | — | ✔ | N/A |
