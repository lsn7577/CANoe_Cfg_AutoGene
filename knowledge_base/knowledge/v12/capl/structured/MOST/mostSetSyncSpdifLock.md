# mostSetSyncSpdifLock

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetSyncSpdifLock(long channel, long mode)
```

## Description

The function locks the internal S/PDIF timing generator on the S/PDIF input data stream.

Unlock the timing generator if frame synchronization is not possible due to a closed loop configuration. A closed loop means that the S/PDIF input signal is locked through an external S/PDIF device on the S/PDIF output of the bus interface.

## Return Values

See error codes

## Example

Use Cases:

External S/PDIF source device connected to the S/PDIF In connector of the VN2610

In this case the VN2610 is S/PDIF Slave (set by mostSetSyncSpdifMode()). In case the VN2610 is configured as TimingSlave it automatically locks the internal S/PDIF timing generator on the S/PDIF input data stream. As TimingMaster the there are two possibilities for configuring the VN2610: Please refer to the example given for mostSetClockSource()).

External S/PDIF source and sink device connected to the S/PDIF In and Out connector of the VN2610

This is not the tyical use case but in case of synchronization problems (mentioned above) the timing generator has to be separated from the S/PDIF input data stream.

More S/PDIF examples see CANoe online help MOST Access to Digital Audio Channels (S/PDIF In and Out).

```c
on key 's'
{
  long channel = 1;
  mostSetSyncSpdifLock( channel, 0 );
}
```

## Availability

| Since Version |
|---|
