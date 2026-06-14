# Iso11783EnableNameManagement

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783EnableNameManagement( dword ecuHandle, dword enable );
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

| Since Version |
|---|
