# FDXTriggerDataGroup

> Category: `Other` | Type: `function`

## Syntax

```c
long FDXTriggerDataGroup (WORD goupID)
```

## Description

This function triggers the transmission of a data group via CANoe FDX protocol.

## Return Values

0: Success

## Example

```c
// CANoe FDX data exchange synchronously to FlexRay cycle
// Whenever slot 5 of the FlexRay cycle will be reached, the FDX data group 10 is transmitted one time 

on frSlot 5
{
   FDXTriggerDataGroup(10);
}
```

## Availability

| Since Version |
|---|
