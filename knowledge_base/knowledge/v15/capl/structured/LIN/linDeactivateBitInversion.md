# linDeactivateBitInversion

> Category: `LIN` | Type: `function`

## Syntax

```c
long LINDeactivateBitInversion();
```

## Description

With this function it is possible to cancel a previously activated bits inversion for LIN header or response. This function is useful when after calling linInvertHeaderBit() no header occurred yet on the bus or when after calling linInvertRespBit() no frame occurred yet.

## Return Values

On success a value unequal to zero, otherwise zero.

## Example

Deactivate previous bit inversion

```c
on key 'd'
{
   if (0==linDeactivateBitInversion())
   {
      write("CAPL: Bit inversion deactivation failure!");
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.2 | — | — | — | 1.0 |
| Restricted To | — | LIN Real bus mode | — | — | — | LIN Real bus mode |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
