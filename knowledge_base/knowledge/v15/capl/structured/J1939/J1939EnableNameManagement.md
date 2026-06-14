# J1939EnableNameManagement

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939EnableNameManagement( dword ecuHandle, dword enable )
dword J1939EnableNameManagement( dword ecuHandle, dword enable, dword bitMask )
```

## Description

This function activates the name management of a node.

Not until the name management is activated another node can change the device name of this node by sending a name management message.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| enable | 1: activate the name management 0: deactivates the name management |
| bitMask | parts of the device name that are allowed to be changed bit 0 (LSB): Arbitrary Address Capable bit 1: Industry Group bit 2: System Instance bit 3: System bit 4: Function bit 5: Function Instance bit 6: ECU Instance bit 7 (MSB): Manufacturer Code |

## Return Values

0 or error code

## Example

```c
LONG busHandle;
LONG ecuAddress;
LONG ecuHandle;
char deviceName[8]; // device name of the node

busHandle  = J1939GetBus( "J1939" );
ecuAddress = dbNode.NmStationAddress; // dbNode must be configured in database

J1939MakeName(
  deviceName, dbNode.NmJ1939AAC,
  dbNode.NmJ1939IndustryGroup,
  dbNode.NmJ1939SystemInstance,
  dbNode.NmJ1939System,
  dbNode.NmJ1939Function,
  dbNode.NmJ1939FunctionInstance,
  dbNode.NmJ1939ECUInstance,
  dbNode.NmJ1939ManufacturerCode,
  dbNode.NmJ1939IdentityNumber );
ecuHandle = J1939CreateECU( busHandle, deviceName );

if (ecuHandle != 0)
{
  /* allow every component to be changed except arbitrary address capable flag */
J1939EnableNameManagement(ecuHandle, 1, 0xFE);
 J1939ECUGoOnline( ecuHandle, ecuAddress );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | J1939 | J1939 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
