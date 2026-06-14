# GNSSGetAddress

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSGetAddress( dword mask, byte [8] name)
```

## Description

The function returns a network address with which a control device that is described by the function parameters logged on to the network.

If no device is found for the described functionality, the NULL address (255) is returned. If the function fails, 0xFFFFFFFF will be returned.

The mask parameter is used to specify which parts of the name will be taken into consideration. To use the entire name, the value 0x1FF must be used for mask. The values of the following table can be linked with a logical OR to make it possible to consider only parts of the name. If the name applies to multiple nodes on the bus, only the address of the first node is returned.

0x001

Self-configurable

0x002

Industry group

0x004

Device class instance

0x008

Device class

0x010

Function

0x020

Function instance

0x040

ECU instance

0x080

Manufacturer code

0x100

Identity number

## Return Values

Address or 0xFFFFFFFF

## Example

```c
dword address;
address = GNSSGetAddress( 0x1FF, name );
```

## Availability

| Since Version |
|---|
