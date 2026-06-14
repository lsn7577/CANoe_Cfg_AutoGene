# Iso11783CreateECU

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783CreateECU( dword busHandle, char deviceName[] );
```

## Description

This function sets up a logical node within a CANoe network node. Several logical nodes can be generated for each CANoe network node. At least one logical node must be generated for each CANoe network node.

The deviceName parameter is used to transfer the device name (see Iso11783 naming convention) of the logical node.

With the parameter busName, you must select a bus on which this ECU will be used. Care should be taken not to assign any name twice on one network (Iso11783 specification). It is allowed to assign an ECU name twice, if another bus is used. On this way a gateway capability can be reached. The joint handling of these instances shall be tasked by the application. Only buses can be used, which are assigned in the Simulation Setup. If the node is assigned only to one bus, the busname "default" can be used.

The handle serves as an unique key to the generated ECU and must therefore be saved for as long as the logical node is in use.

## Return Values

Handle to the generated (logical) ECU or 0 if an error occurred

## Example

```c
ecuHdl = Iso11783CreateECU( "default", name);
```

## Availability

| Since Version |
|---|
