# mostSetSyncSpdifMode

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetSyncSpdifMode(long channel, long mode)
```

## Description

Sets the timing mode for the S/PDIF signal.

## Return Values

See error codes

## Example

Use Cases:

External S/PDIF sink device connected to the S/PDIF Out connector of the VN2610

In this case the VN2610 is S/PDIF Master and the S/PDIF mode has to be set accordingly (mode = 1).

External S/PDIF source device connected to the S/PDIF In connector of the VN2610

In this case the VN2610 is S/PDIF Slave and the S/PDIF mode has to be set accordingly (mode = 0).

More S/PDIF examples see CANoe online help MOST Access to Digital Audio Channels (S/PDIF In and Out).

```c
on key 's'
{
  long channel = 1;
  mostSetSyncSpdifMode( channel, 1 );
}

on key 's'
{
  long channel = 1;
  mostSetSyncSpdifMode( channel, 0 );
}
```

## Availability

| Since Version |
|---|
