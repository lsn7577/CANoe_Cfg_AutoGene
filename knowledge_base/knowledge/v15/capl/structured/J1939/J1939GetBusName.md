# J1939GetBusName

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetBusName( dword busHandle, dword bufferSize, char buffer[] );
```

## Description

Gets a bus name.

## Parameters

| Name | Description |
|---|---|
| busHandle | bus handle, see also J1939GetBus |
| bufferSize | size of buffer in Bytes |
| buffer | bus name is copied into this buffer |

## Example

```c
char busName[32];
J1939GetBusName( busHandle, 
 elCount(busName), busName );
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
