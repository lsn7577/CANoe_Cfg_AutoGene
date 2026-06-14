# GNSSAppCmdAddrIndication

> Category: `J1939` | Type: `function`

## Syntax

```c
void GNSSAppCmdAddrIndication( long newAddress )
```

## Description

This function indicates that a new address has been assigned to the node by the “Commanded Address” parameter group. The node must log on to the bus again with the assigned address (see GNSSStartUp).

## Return Values

—

## Example

```c
void GNSSAppCmdAddrIndication( LONG newAddr )
{
  GNSSShutDown();
  GNSSStartUp( gName, newAddr );
}
```

## Availability

| Since Version |
|---|
