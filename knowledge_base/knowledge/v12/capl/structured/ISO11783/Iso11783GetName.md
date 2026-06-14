# Iso11783GetName

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetName( char[] busName, dword componentMask, char deviceName[] );
```

## Description

This function returns the name of a device that was logged onto the network with address. The function works with a global table that contains all node names and addresses logged onto the network.

If no device is logged onto the network with address #10 then name={8*DEFAULT_VALUE}. In this version DEFAULT_VALUE is 0.

## Return Values

0 - success or error code

## Example

```c
char deviceName[8];
Iso11783GetName( "default", 
 0, deviceName );
```

## Availability

| Since Version |
|---|
