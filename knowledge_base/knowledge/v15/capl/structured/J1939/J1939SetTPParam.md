# J1939SetTPParam

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939SetTPParam( dword ecuHandle, dword what, dword value );
```

## Description

Changing transport protocol settings.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| Index | Description Value Range Initial Value |
| 1 | Maximum number of bytes, which can be transferred 8 < value < 117440505 100 MByte |
| 2 | Number of packets, which are requested by CTS 1 < value < 255 1 |
| 3 | Number of packets, which are requested by ECTS (Extended TP) 1 < value < 255 64 |
| 8 | Number of packets, which is used with RTS 1 < value < 255 255 |
| 10 | Set the used debug level 0 < value < 3 2 |
| 11 | Use of network management 0:deactivate network management 1: activate network management 0 < value < 1 1 |
| 12 | target address, which is used for BAM 0: target address is 0xFF 1: specific target address is used 0 < value < 1 0 |
| 13 | priority used by the transport protocol 0 < value < 7 7 |
| value | new value |

## Return Values

0 on success or error code

## Example

```c
J1939SetTPParam(ecuHdl, 
 1, 32*1024 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
