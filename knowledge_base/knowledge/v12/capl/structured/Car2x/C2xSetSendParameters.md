# C2xSetSendParameters

> Category: `Car2x` | Type: `function`

## Syntax

```c
C2xSetSendParameters(LONG appChannel, LONG txPower, LONG antenna, LONG dataRate, LONG expiry)
```

## Description

Set transmission relevant send parameters.

This method allows to redefine some or all transmission related parameters on the fly; for all following transmissions on a specific VN4610 channel those new default values will be used.

In fact the method overwrites the corresponding internal configuration settings provided by the setup-dialog.

To set just a subset of the parameters the value <-1> can be used for antenna, dataRate and expiry to leave the corresponding parameters of the configuration unchanged.

Note: This method can only be used with VN4610 hardware.

## Return Values

0 or error code as in C2xConfigureChannel.

## Example

```c
on key '1'
{
  Write("Set SendParameters for Ch1 to -10dBm  Ant2, 9Mbps; don’t change expiry ");
  C2xSetSendParameters(1, -10, 2, 9, -1);
}
```

## Availability

| Since Version |
|---|
