# OnMostTxLight

> Category: `MOST` | Type: `function`

## Syntax

```c
OnMostTxLight(long mode)
```

## Description

The event procedure is called as soon as the light status of the fibre optical transmitter (FOT) is switched.

The event procedure is only called if the light status has been switched by the application (see also mostSetTxLight).

## Parameters

| Name | Description |
|---|---|
| 0 | FOT disabled: Tx light off |
| 1 | FOT enabled: TimingMaster: Modulated light on TimingSlave/Bypass: Tx light = Rx light |
| 2 | FOT enabled: Constant light on |

## Return Values

—

## Availability

| Since Version |
|---|
