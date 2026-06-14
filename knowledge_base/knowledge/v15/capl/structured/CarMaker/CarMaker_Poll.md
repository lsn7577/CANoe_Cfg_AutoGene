# CarMaker_Poll

> Category: `CarMaker` | Type: `function`

## Syntax

```c
long CarMaker_Poll(char host[], char user[]);
```

## Description

Manages the internal state and updates the CANoe system variables. If the polling cycle is set to zero in the configuration dialog, automatic polling is disabled, and this function must be called regularly.

If the polling cycle is set in the configuration dialog, the automatic polling is enabled and calling this function is not required.

The function can also be used to get the current APO return code.

## Return Values

APO return code

## Example

```c
  // get the current error status
  gErrorState = CarMaker_Poll();
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | — | — | — | 5.0 |
| Restricted To | — | CarMaker | — | — | — | CarMaker |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
