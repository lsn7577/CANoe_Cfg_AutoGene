# Iso11783MakeName

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783MakeName( char[] retDeviceName, long selfConfiguring, long industryGroup, long deviceClassInstance, long deviceClass, long function, long functionInstance, long ECUInstance, long manufacturerCode, long identityNumber );
```

## Description

This function creates a Iso11783 device name.

The parameter retDeviceName must be an array with size 8. It will be filled with the device name.

## Return Values

—

## Example

```c
char name[8];
Iso11783MakeName( name, 1, 2, 3, 4, 5, 6, 7, 8, 9);
```

## Availability

| Since Version |
|---|
