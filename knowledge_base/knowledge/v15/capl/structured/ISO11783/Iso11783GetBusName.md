# Iso11783GetBusName

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetBusName( dword busHandle, dword bufferSize, char buffer[] );
```

## Description

Gets a bus name.

## Parameters

| Name | Description |
|---|---|
| busHandle | Bus handle, see also Iso11783GetBus |
| bufferSize | Size of buffer in Bytes |
| buffer | Bus name is copied into this buffer |

## Return Values

0 or error code

## Example

```c
char busName[32];
Iso11783GetBusName( busHandle, 
 elCount(busName), busName );
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
