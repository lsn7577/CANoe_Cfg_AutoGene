# Iso11783GetRxData

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetRxData( dword bufferSize, char buffer[] );
```

## Description

An auxiliary function for receiving PG data within a callback function.

The DLL interface will not permit you to transfer data arrays via callback. Therefore it serves the purpose of "retrieving" data from the node layer. Since this function is called within a callback, there is no need to transfer an ECU handle. If the function is called from outside of a callback, the call has no effect.

## Parameters

| Name | Description |
|---|---|
| bufferSize | Size of the buffer |
| buffer | Buffer which should receive the data |

## Return Values

Number of bytes copied

## Example

```c
char data[100];
dword count;

count = Iso11783GetRxData( elCount(data), data );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 6.1 | 13.0 | — | — | — |
| Restricted To | — | Iso11783 | Iso11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
