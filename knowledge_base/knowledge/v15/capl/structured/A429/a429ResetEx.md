# a429ResetEx

> Category: `A429` | Type: `function`

## Syntax

```c
long a429ResetEx( long channel );
```

## Description

Re-initialize the selected channel with the active channel parameters. The active channel parameters are read with a429GetConfiguration and modified with a429SetConfiguration.

Note, that the channel is reset. The transmit queue and the hardware schedule table is emptied for this channel.

## Parameters

| Name | Description |
|---|---|
| channel | valid channel number |

## Example

```c
on key 'r'
{
  if (a429ResetEx(RxChannel)) {
    write("reset channel '%d' OK", RxChannel);
  }
  else {
    write("reset channel '%d' failed", RxChannel);
  }

  if (a429ResetEx(TxChannel)) {
    write("reset channel '%d' OK", TxChannel);
  }
  else {
    write("reset channel '%d' failed", TxChannel);
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
