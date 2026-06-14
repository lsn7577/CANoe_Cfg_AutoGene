# linSetMasterResistor

> Category: `LIN` | Type: `function`

## Syntax

```c
long linSetMasterResistor (long onOff);
```

## Description

Enables or disables the internal master resistor of the LIN hardware interface.

## Parameters

| Name | Description |
|---|---|
| onOff | 1: Switch the resistor on 0: Switch the resistor off |

## Return Values

If successful a value unequal to zero.

## Example

```c
// on pressing key ‘c’ switch on the master resisitor
...
on key 'c'
{
  linSetMasterResisitor (1);
  write("Turn Resistor On");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 | 8.2 | — | — | — | 1.1 |
| Restricted To | LIN | LIN | — | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
