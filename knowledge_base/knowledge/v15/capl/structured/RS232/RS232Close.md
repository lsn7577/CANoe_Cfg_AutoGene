# RS232Close

> Category: `RS232` | Type: `function`

## Syntax

```c
dword RS232Close( dword port );
```

## Description

Closes a serial port.

The serial port will be closed for all nodes. One and the same port may be closed by several nodes (or repetitively). After closure other programs may use the serial port.

After closing the serial port the configuration of the port is lost. The next time the port is opened it will be configured with the system default.

## Parameters

| Name | Description |
|---|---|
| port | A number between 1 and 255 identifying a serial port. |

## Example

```c
if ( 1==RS232Close(1) ) write(“It works with port 1.”);
```

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
