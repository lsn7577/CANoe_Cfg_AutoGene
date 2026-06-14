# ILControlWait

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long ILControlWait(char aNodeName[])
```

## Description

Stops the interaction layer of the selected simulation node.This function influences a simulation node with an assigned CANoe interaction layer.

## Return Values

0: No error.

## Example

```c
// stops the interaction layer of ECU A for 2000ms.

variables {
  msTimer WaitTimer;
}

On Key 'x' {
  ILControlWait ("ECU_A");
  SetTimer(WaitTimer,2000);
}

On Timer WaitTimer {
  ILControlResume ("ECU_A");
}
```

## Availability

| Up to Version |
|---|
