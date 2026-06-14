# ILNodeDisturbCounter

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeDisturbCounter(dbMsg aMessage, char aSigGroupName[], long counterType, long disturbanceMode, long disturbanceCount, long disturbanceValue, long continueMode); // form 1
long ILNodeDisturbCounter(char aMessageName[], char aSigGroupname[], long counterType, long disturbanceMode, long disturbanceCount, long disturbanceValue, long continueMode); // form 2
long ILNodeDisturbCounter (char sigGroupName[], long type, long disturbanceMode, long disturbanceCount, long disturbanceValue, long continueMode); // form 3
```

## Description

This function modifies the counter. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer.

## Parameters

| Name | Type | Description |
|---|---|---|
| aMessage |  | Message or PDU that should be modified. |
| aMsgName |  | Name of the message or PDU that should be modified. Supported qualification patterns for form 2: [DBName::][NodeName::]aMessageName |
| aSigGroupName |  | Some systems assign a counter to signal group. When specifing the signal group you can apply the disturbance to a dedicated signal group within a message or PDU. Use an empty character array if the counter of the whole message or PDU should be affected. Supported qualification patterns for form 3: [DBName::][NodeName::][MessageName::]aSignalgroupName |
| counterType |  | The possible values are described in the corresponding OEM Package manual. |
| 0 | Value | The disturbance uses the value in disturbanceValue as counter. |
| 1 | Freeze | The current counter value is transmitted. |
| 2 | Random | A random value is transmitted as counter. |
| 3 | Offset | The counter is incremented with the value in disturbanceValue. |
| -1 |  | Infinite. |
| 0 |  | Stops the disturbance, e.g.a infinite disturbance. |
| n |  | Number of disturbances. |
| disturbanceValue |  | This value is used in combination with the disturbanceMode. |
| 0 | CorrectCounter | The counter will be incremented with counter value + number of disturbances. |
| 1 | LastValidCounter | The counters next value bases on the last value before the disturbance has started. |
| 2 | LastValue | The counter increments the last counter value (last disturbance value). |

## Example

```c
// Disturbs the PDU counter, disturbance pattern: 100x random value,
// after the disturbance the counters next value bases on
// the last value before the disturbance has started.

variables {
  long countertype =0;
  long disturbanceMode= 2;  // A random value is transmitted as counter.
  long disturbanceCoun=100;
  long disturbanceValue=0;  // value will be ignored due to disturbance mode
  long continueMode=1;      // The counters next value bases on the last value
                            // before the disturbance has started.
}

on key 'a'{
  ILNodeDisturbCounter("PDU_A", counterType, disturbanceMode, disturbanceCount, disturbanceValue, continueMode);
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
