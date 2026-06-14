# J1939EnableNameManagement

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939EnableNameManagement( dword ecuHandle, dword enable )
```

## Description

This function activates the name management of a node.

Not until the name management is activated another node can change the device name of this node by sending a name management message.

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

| Since Version |
|---|
