# GNSSGetName

> Category: `J1939` | Type: `function`

## Syntax

```c
dword GNSSGetName( dword addr, byte name[] );
```

## Description

The function returns the J1939 device name of a control device that was logged on to the network with addr. The function works with a global table containing all node names and addresses logged on to the network.

## Return Values

error code

## Example

```c
char name[8];
GNSSGetName( 10, name );
```

## Availability

| Since Version |
|---|
