# GNSSStartUp

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSStartUp( byte name[8], uint address )
```

## Description

This function sets up a logical node within a CANoe network node. The name parameter is used to transfer the J1939 device name of the logical node. Care should be taken not to assign any name twice on the network.

## Parameters

| Name | Description |
|---|---|
| name | Name of the device |
| address | Address of the device |

## Return Values

Error code

## Example

```c
char name[8];
GNSSMakeName( name, 1, 0, 0, 0, 28, 0, 0, 0, 0);
GNSSStartUp( 
 name, 3 );
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | 13.0 | — | — | — |
| Restricted To | — | J1939 ISO11783 | J1939 ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
