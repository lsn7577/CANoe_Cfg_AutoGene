# mostSetClockSource

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetClockSource(long channel, long source)
```

## Description

Sets the clock source for the MOST timing master. The function has no effect if the bus interface is configured as MOST timing slave.

## Return Values

See error codes

## Example

Use case: External S/PDIF source device connected to the S/PDIF In connector of the VN2610

Typically the internal oscillator is used as clock source, since most S/PDIF source devices do not generate a S/PDIF signal with the same clock as the MOST clock (44,1 / 48 kHz).

In some special cases, e.g. for testing purpose it is possible to synchronize the timing master clock to S/PDIF input signal.

More S/PDIF examples see CANoe online help MOST Access to Digital Audio Channels (S/PDIF In and Out).

```c
// use internal oscillators timing master clock
on key 's'
{
  long channel = 1;

  // configure hardware interface as S/PDIF slave
  mostSetSyncSpdifMode( channel, 0 );
  mostSetSyncSpdifLock( channel, 1 );

  // set the clock source
  mostSetClockSource( channel, 0 );
}

// synchronize the timing master clock to the S/PDIF input signal
on key 's'
{
  long channel = 1;

  // configure hardware interface as S/PDIF slave
  mostSetSyncSpdifMode( channel, 0 );

  // set the clock source
  mostSetClockSource( channel, 1 );
}
```

## Availability

| Since Version |
|---|
