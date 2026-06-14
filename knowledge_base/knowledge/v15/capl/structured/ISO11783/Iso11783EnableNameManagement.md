# Iso11783EnableNameManagement

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783EnableNameManagement( dword ecuHandle, dword enable );
dword Iso11783EnableNameManagement( dword ecuHandle, dword enable, dword bitMask );
```

## Description

This function activates the name management of a node.

Not until the name management is activated another node can change the device name of this node by sending a name management message.

## Parameters

| Name | Description |
|---|---|
| ecuHandle | ECU handle |
| enable | 1: activate the name management 0: deactivates the name management |
| bitMask | Parts of the device name that are allowed to be changed bit 0 (LSB): Arbitrary Address Capable bit1: Industry Group bit 2: System Instance bit 3: System bit 4: Function bit 5: Function Instance bit 6: ECU Instance bit 7 (MSB): Manufacturer Code |

## Return Values

0 or error code

## Example

```c
LONG busHandle;
LONG ecuAddress;
LONG ecuHandle;
char deviceName[8]; // device name of the node

busHandle  = Iso11783GetBus( "ISO11783" );
ecuAddress = dbNode.NmStationAddress; // dbNode must be configured in database

Iso11783MakeName(
  deviceName, dbNode.NmIso11783AAC,
  dbNode.NmIso11783IndustryGroup,
  dbNode.NmIso11783SystemInstance,
  dbNode.NmIso11783System,
  dbNode.NmIso11783Function,
  dbNode.NmIso11783FunctionInstance,
  dbNode.NmIso11783ECUInstance,
  dbNode.NmIso11783ManufacturerCode,
  dbNode.NmIso11783IdentityNumber );
ecuHandle = Iso11783CreateECU( busHandle, deviceName );

if (ecuHandle != 0)
{
  /* allow every component to be changed except arbitrary address capable flag */
   Iso11783EnableNameManagement(ecuHandle, 1, 0xFE);
   Iso11783ECUGoOnline( ecuHandle, ecuAddress );
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.0 | 13.0 | — | — | — |
| Restricted To | — | Iso11783 | Iso11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
