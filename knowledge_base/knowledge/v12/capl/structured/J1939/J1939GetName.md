# J1939GetName

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetName( char[] busName, dword componentMask, char deviceName[] );
```

## Description

This function returns the name of a device that was logged onto the network with address. The function works with a global table that contains all node names and addresses logged onto the network.

If no device is logged onto the network with address #10 then name={8*DEFAULT_VALUE}. In this version DEFAULT_VALUE is 0.

## Example

```c
char deviceName[8];
J1939GetName( "default", 
 0, deviceName );
```

## Availability

| Since Version |
|---|
