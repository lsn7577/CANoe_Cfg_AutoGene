# J1939GetName

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetName( char[] busName, dword componentMask, char deviceName[] );
dword J1939GetName( long busHandle, dword componentMask, char deviceName[] );
```

## Description

This function returns the name of a device that was logged onto the network with address. The function works with a global table that contains all node names and addresses logged onto the network.

If no device is logged onto the network with address #10 then name={8*DEFAULT_VALUE}. In this version DEFAULT_VALUE is 0.

## Parameters

| Name | Description |
|---|---|
| busName | bus name or "default" |
| busHandle | bus handle, see J1939GetBus |
| componentMask | address of the node |
| deviceName | buffer to which the data is copied (size: 8 Byte). |

## Example

```c
char deviceName[8];
J1939GetName( "default", 
 0, deviceName );
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
