# ILNodeDisturbSignalGroupUpdateBit

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeDisturbSignalGroupUpdateBit(dbMsg aMessage, char aSigGroupName[], long disturbanceMode, long disturbanceCount, long disturbanceValue); // form 1
long ILNodeDisturbSignalGroupUpdateBit(char aMessageName[], char aSigGroupName[], long disturbanceMode, long disturbanceCount, long disturbanceValue); // form 2
long ILNodeDisturbSignalGroupUpdateBit (char aSignalGroupName[], long disturbanceMode, long disturbanceCount, long disturbanceValue); // form 3
```

## Description

Modifies the update bit of a signal group. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer

## Parameters

| Name | Type | Description |
|---|---|---|
| aMessage |  | The symbolic name of message in the database containing the signal group. |
| aMessageName |  | The name of message in the database containing the signal group. Supported qualification patterns for form 2: [DBName::][NodeName::]aMessageName |
| aSigGroupName |  | Name of the signal group using an update bit. Supported qualification patterns for form 3: [DBName::][NodeName::][MessageName::]aSignalgroupName |
| 0 | Value | The disturbance uses the value in disturbanceValue as update bit. |
| 1 | Freeze | The current update bit value is transmitted. |
| 2 | Random | A random value is transmitted as update bit. |
| -1 |  | Infinite. |
| 0 |  | Stops the disturbance, e.g.a infinite disturbance. |
| n |  | Number of disturbances. |
| disturbanceValue |  | This value is used in combination with the disturbanceMode. |

## Example

```c
// Sets the Signal Group Update Bit to 0

variables {
  long disturbanceMode  = 0; // The disturbance uses the value in disturbanceValue as Update Bit.
  int disturbanceCount  = 100;
  long disturbanceValue = 0;
}

on key 'a'{
  ILNodeDisturbSignalGroupUpdateBit(Message_A, "SignalGroup_A", disturbanceMode, disturbanceCount, disturbanceValue);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 SP4: form 1-2 8.5: form 3 | 14 | 14 | — | — |
| Restricted To | — | CAN FlexRay | CAN FlexRay | CAN FlexRay | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | — | N/A |
