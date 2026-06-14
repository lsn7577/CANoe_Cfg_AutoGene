# J1939GetRxData

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetRxData( dword bufferSize, char buffer[] );
```

## Description

An auxiliary function for receiving PG data within a callback function.

The DLL interface will not permit you to transfer data arrays via callback. Therefore it serves the purpose of "retrieving" data from the node layer. Since this function is called within a callback, there is no need to transfer an ECU handle. If the function is called from outside of a callback, the call has no effect.

## Parameters

| Name | Description |
|---|---|
| bufferSize | size of the buffer |
| buffer | buffer which should receive the data |

## Return Values

number of bytes copied

## Example

```c
char data[100];
dword count;

count = J1939GetRxData( elCount(data), data );
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
