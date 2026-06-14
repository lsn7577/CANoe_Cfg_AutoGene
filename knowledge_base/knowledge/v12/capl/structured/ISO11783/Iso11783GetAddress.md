# Iso11783GetAddress

> Category: `ISO11783` | Type: `function`

## Syntax

```c
dword Iso11783GetAddress( char[] busName, dword componentMask, char deviceName[8] );
```

## Description

This function returns a network address with which a device that is described by the function parameters logged onto the network.

## Return Values

Address of the node or Null Address (0xFE) if no device is found or FFFFFFFFh if the functions fails.

## Example

```c
char deviceName[8] = { 0, 0, 0, 0, 0 ,0, 0, 0};
address = Iso11783GetAddress( "default", 
 0x1ff, deviceName);
```

## Availability

| Since Version |
|---|
