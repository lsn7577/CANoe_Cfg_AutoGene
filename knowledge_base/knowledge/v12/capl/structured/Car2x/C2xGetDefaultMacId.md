# C2xGetDefaultMacId

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetDefaultMacId( byte macId[] );
```

## Description

This function reads the MAC-ID of a WLAN interface.

## Return Values

0 or error code.

## Example

```c
on start
{
  byte macId[6];
  if (C2xGetDefaultMacId( macId ) == 0)
  {
    write( "MAC ID is %.2X:%.2X:%.2X:%.2X:%.2X:%.2X:", macId[0], macId[1], macId[2], macId[3], macId[4], macId[5] );
  }
}
```

## Availability

| Since Version |
|---|
