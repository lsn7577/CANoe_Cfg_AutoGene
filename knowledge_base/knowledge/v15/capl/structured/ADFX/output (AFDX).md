# output (AFDX)

> Category: `ADFX` | Type: `function`

## Syntax

```c
void output (a664Message aMessage) (1)
void output (a664Frame aFrame) (2)
```

## Description

This function outputs the object from the program block of the analysis branch. Use output inside the appropriate event procedure in order to forward the event to the next block in the analysis branch. If the function is not called, then the event is not forwarded. Thus, events will be filtered by the CAPL program when omitting this function.

The function must not be used in the Simulation Setup branch. For transmitting an object of type a664Frame or a664Message use the functions A664TriggerFrame and A664TriggerMessage.

## Return Values

—

## Example

```c
on a664Message * {
  #if MEASUREMENT_SETUP
  output(this);
  #endif
}

// or on frame level

on a664Frame * {
  #if MEASUREMENT_SETUP
  output(this);
  #endif
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0: 1, 2 | 9.0: form 1, 2 | — | — | — | — |
| Restricted To | AFDX | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | — | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
