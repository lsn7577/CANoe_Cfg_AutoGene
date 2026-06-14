# Iso11783GetName

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetName( char[] busName, dword componentMask, char deviceName[] );
dword Iso11783GetName( long busHandle, dword componentMask, char deviceName[] );
```

## Description

This function returns the name of a device that was logged onto the network with address. The function works with a global table that contains all node names and addresses logged onto the network.

If no device is logged onto the network with address #10 then name={8*DEFAULT_VALUE}. In this version DEFAULT_VALUE is 0.

## Parameters

| Name | Description |
|---|---|
| busName | Bus name or "default" |
| busHandle | Bus handle, see Iso11783GetBus |
| componentMask | Address of the node |
| deviceName | Buffer to which the data is copied (size: 8 Byte). |

## Return Values

0 - success or error code

## Example

```c
char deviceName[8];
Iso11783GetName( "default", 
 0, deviceName );
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
