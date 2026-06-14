# EthGetMacId

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long EthGetMacId( byte macId[] );
```

## Description

This function reads the MAC-ID of the Ethernet interface.

## Example

```c
on start

{

  BYTE macId[6];
 
  if (EthGetMacId( macId ) == 0) 
  {

    write( "MAC ID is %.2X:%.2X:%.2X:%.2X:%.2X:%.2X:", macId[0], macId[1], 
    macId[2],  macId[3], macId[4], macId[5] );

  }
}
```

## Availability

| Up to Version |
|---|
