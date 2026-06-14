# a429InitPayload

> Category: `A429` | Type: `function`

## Syntax

```c
long a429InitPayload (a429Word myA429word)
```

## Description

Initialize the payload of an existing a429word using the current values of corresponding signals from SignalServer.

This can be used to initialize a message from scratch to the StartValues of the StartValue-table in the Init-section, or to assign the current signal values to the payload during any time of measurement.

## Parameters

| Name | Description |
|---|---|
| myA429Word | message which should be initialized with current signal values |

## Example

```c
variables
{
  a429Word *msg = { msgChannel = 1};
}
on key '1'
{
  a429InitPayload(msg);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 10.0 | 10.0 | — | — | — | — |
| Restricted To | A429 | A429 | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
