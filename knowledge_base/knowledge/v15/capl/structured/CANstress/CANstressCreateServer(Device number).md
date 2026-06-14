# CANstressCreateServer(Device number)

> Category: `CANstress` | Type: `function`

## Syntax

```c
long CANstressCreateServer (dword deviceNr);
```

## Description

Starts the CANstress software and establishes a connection to this COM server via the COM interface. The COM server generated only establishes a connection to the CANstress device defined in deviceNr. Connected CANstress devices are mapped to a number using the canstress.INI file. You will find this file in the CANstress software’s installation directory. If the call is successful, the device defined in deviceNr will be set as the current device.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.0 | — | — | — | 1.1 |
| Restricted To | — | CAN CANstress | — | — | — | CAN CANstress |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
