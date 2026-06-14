# J1939GetAddress

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetAddress( char[] busName, dword componentMask, char eviceName[8] );
dword J1939GetAddress( long busHandle, dword componentMask, char deviceName[8] );
```

## Description

This function returns a network address with which a device that is described by the function parameters logged onto the network.

## Parameters

| Name | Description |
|---|---|
| busName | bus name or "default" |
| busHandle | bus handle, see J1939GetBus |
| Bit | Description |
| 1 | Self-configurable |
| 2 | Industry group |
| 4 | Device class instance |
| 8 | Device class |
| 16 | Function |
| 32 | Function instance |
| 64 | ECU instance |
| 128 | Manufacturer code |
| 256 | Identity number |
| deviceName | device name |

## Return Values

address of the node or Null Address (0xFE) if no device is found or FFFFFFFFh if the functions fails.

## Example

```c
char deviceName[8] = { 0, 0, 0, 0, 0 ,0, 0, 0};
address = J1939GetAddress( "default", 
 0x1ff, deviceName);
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
