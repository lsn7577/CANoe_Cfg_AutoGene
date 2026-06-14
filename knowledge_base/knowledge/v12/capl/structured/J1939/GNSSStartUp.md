# GNSSStartUp

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSStartUp( byte name[8], uint address )
```

## Description

This function sets up a logical node within a CANoe network node. The name parameter is used to transfer the J1939 device name of the logical node. Care should be taken not to assign any name twice on the network.

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

| Since Version |
|---|
