# Iso11783GetAddress

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetAddress( char[] busName, dword componentMask, char deviceName[8] );
dword Iso11783GetAddress( long busHandle, dword componentMask, char deviceName[8] );
```

## Description

This function returns a network address with which a device that is described by the function parameters logged onto the network.

## Parameters

| Name | Description |
|---|---|
| busName | Bus name or "default" |
| busHandle | Bus handle, see Iso11783GetBus |
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
| deviceName | Device name |

## Return Values

Address of the node or Null Address (0xFE) if no device is found or FFFFFFFFh if the functions fails.

## Example

```c
char deviceName[8] = { 0, 0, 0, 0, 0 ,0, 0, 0};
address = Iso11783GetAddress( "default", 
 0x1ff, deviceName);
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
