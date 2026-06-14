# a429GetConfiguration

> Category: `A429` | Type: `function`

## Syntax

```c
long a429GetConfiguration( long channel, a429settings mySettings );
```

## Description

This function returns the actual channel configuration settings.

## Example

```c
on key 'c'
{
  long channel;
  a429settings mySettings;

  channel = RxChannel;
  if (a429GetConfiguration(channel, mySettings)) {
    write ("parameters of channel '%d', bitrate '%d' (%d .. %d), parity = '%s', flags = '%s'", channel, mySettings.Bitrate, mySettings.RxMinBitrate, mySettings.RxMaxBitrate, ((enum Ea429ParityCtrl)mySettings.Parity).name(), ((enum Ea429SettingsFlags)mySettings.Flags).name());
  }
  else {
    write(" parameters for '%d' not available");
  }
}
```

## Availability

| Since Version |
|---|
