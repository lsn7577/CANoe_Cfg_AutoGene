# linGetMasterResistorState

> Category: `LIN` | Type: `function`

## Syntax

```c
long linGetMasterResistorState();
```

## Description

Returns the internal master resistor’s current state of the LIN interface hardware.

## Example

```c
// on pressing key ‘c’ switch on the master resistor
...
on key 'c'
{
  long ret;
  ret = linGetMasterResistorState();
  write("Resistor State: %d", ret);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 8.2 | 8.2 | 13.0 | — | — | 1.1 |
| Restricted To | LIN | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
