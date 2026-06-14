# setCanCabsMode

> Category: `CAN` | Type: `function`

## Syntax

```c
long setCanCabsMode(long ntype,long nchannel,long nmode,long nflags);
```

## Description

Various CANcabs modes may be set. Replaces the setPortBits functions.

Please note that not all modes set with this functions are supported by all transceivers.

## Return Values

0: ok

## Example

```c
on key 'n'
{
   long ntype, nmode, nchannel, nflags;
   ntype = 0;
   nmode = 0;
   nchannel = 1;
   nflags = 0;
   setCanCabsMode(ntype, nchannel, nmode, nflags);
   write("normal mode");
}
```

## Availability

| Since Version |
|---|
