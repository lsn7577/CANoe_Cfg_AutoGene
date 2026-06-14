# J1939GetAddress

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939GetAddress( char[] busName, dword componentMask, char eviceName[8] );
```

## Description

This function returns a network address with which a device that is described by the function parameters logged onto the network.

## Return Values

address of the node or Null Address (0xFE) if no device is found or FFFFFFFFh if the functions fails.

## Example

```c
char deviceName[8] = { 0, 0, 0, 0, 0 ,0, 0, 0};
address = J1939GetAddress( "default", 
 0x1ff, deviceName);
```

## Availability

| Since Version |
|---|
