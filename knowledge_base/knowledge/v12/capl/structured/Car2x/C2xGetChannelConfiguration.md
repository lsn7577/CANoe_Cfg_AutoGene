# C2xGetChannelConfiguration

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xGetChannelConfiguration(long appChannel, long radioChannel, long txPower, long maxTxPower, long layout, long dataRate, long bandWidth, long txAntenna, long rxAntenna)
```

## Description

Retrieve the current configuration parameters of a specific hardware channel.

This method allows to readout all relevant channel parameters opposite to C2xConfigureChannel

Note: This method can only be used with VN4610 hardware.

## Return Values

0 or error code according to the following.

## Example

```c
on key 'g'
{
  long radioChannel, txPower, maxTxPower, layout, dataRate, bandWidth, txAntenna, rxAntenna, i;
  i = C2xGetChannelConfiguration(1, radioChannel, txPower, maxTxPower, layout, dataRate, bandWidth, txAntenna, rxAntenna);
  if (i != 0)
    Write("C2xGetChannelConfiguration 1 failed with err=%d", i);
  else
    Write("ChannelConfig#1: radio:%d layout:%d txPow:%d maxTxPow:%d rate:%d bandWidth:%d txAnt:%d rxAnt:%d",
      radioChannel, layout, txPower, maxTxPower, dataRate, bandWidth, txAntenna, rxAntenna);
}
```

## Availability

| Since Version |
|---|
