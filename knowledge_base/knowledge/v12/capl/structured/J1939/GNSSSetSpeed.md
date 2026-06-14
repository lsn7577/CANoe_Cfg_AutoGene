# GNSSSetSpeed

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSSetSpeed( double speed )
```

## Description

This function sets the speed at which the GNSS receiver moves. The unit of the parameter depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

error code

## Example

```c
GNSSSetUnits( 2 );  // set nautic 
 system
GNSSSetSpeed( 
 20 ); // new speed: 20 Knots
```

## Availability

| Since Version |
|---|
