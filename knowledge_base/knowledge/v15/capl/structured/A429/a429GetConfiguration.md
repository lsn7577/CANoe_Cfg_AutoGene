# a429GetConfiguration

> Category: `A429` | Type: `function`

## Syntax

```c
long a429GetConfiguration( long channel, a429settings mySettings );
```

## Description

This function returns the actual channel configuration settings.

## Parameters

| Name | Description |
|---|---|
| channel | valid channel number |
| mySettings | variable to store channel parameters |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.5 | 8.5 | — | — | — | — |
| Restricted To | A429 | A429 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
