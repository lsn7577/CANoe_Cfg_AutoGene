# ILEnableTimingEvtTrg

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILEnableTimingEvtTrg(char pduName[], int enable);
```

## Description

Controls the event triggered timing of PDUs. The event triggered timing can be enabled/disabled.This function influences a simulation node with an assigned CANoe interaction layer.

## Return Values

0: No error.

## Example

```c
// Disables the PDU Timing for 2000 ms
variables {
  int enable = 0;
  msTimer WaitTimer;
}
on key 'a'{
  enable = 0;
  ILEnableTimingEvtTrg ("PDU_A", enable);
  SetTimer(WaitTimer,2000);
}
On Timer WaitTimer {
  enable = 1;
  ILEnableTimingEvtTrg ("PDU_A", enable);
}
```

## Availability

| Since Version |
|---|
