# GNSSSetUnits

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetUnits( dword unitType )
```

## Description

This function determines the system of units of measure that will be used by the various other functions.

Units of measure:

When the node is set up, the metric system for units of measures is set.

## Return Values

error code

## Example

```c
// set nautic system
GNSSSetUnits( 2 );
```

## Availability

| Since Version |
|---|
