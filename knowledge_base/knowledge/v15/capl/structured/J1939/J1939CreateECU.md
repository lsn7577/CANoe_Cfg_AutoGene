# J1939CreateECU

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939CreateECU( dword busHandle, char deviceName[] );
dword J1939CreateECU( char busName[], char deviceName[] );
```

## Description

This function sets up a logical node within a CANoe network node. Several logical nodes can be generated for each CANoe network node. At least one logical node must be generated for each CANoe network node.

The deviceName parameter is used to transfer the device name (see J1939 naming convention) of the logical node.

With the parameter busName, you must select a bus on which this ECU will be used. Care should be taken not to assign any name twice on one network (J1939 specification). It is allowed to assign an ECU name twice, if another bus is used. On this way a gateway capability can be reached. The joint handling of these instances shall be tasked by the application. Only buses can be used, which are assigned in the Simulation Setup. If the node is assigned only to one bus, the busname "default" can be used.

The handle serves as an unique key to the generated ECU and must therefore be saved for as long as the logical node is in use.

## Parameters

| Name | Description |
|---|---|
| busHandle | current bus handle |
| deviceName | 64-bit device name |
| busName | bus name (or use "default") |

## Return Values

handle to the generated (logical) ECU or 0 if an error occurred

## Example

```c
ecuHdl = J1939CreateECU( "default", name);
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
