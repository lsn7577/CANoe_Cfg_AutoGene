# ILNodeDisturbChecksum

> Category: `CANoeIL` | Type: `function`

## Syntax

```c
long ILNodeDisturbChecksum(dbMsg aMessage, char aSigGroupName[], long checksumType, long disturbanceMode, long disturbanceCount, long disturbanceValue); // form 1
long ILNodeDisturbChecksum(char aMessageName[], char aSigGroupName[], long checksumType, long disturbanceMode, long disturbanceCount, long disturbanceValue); // form 2
long ILNodeDisturbChecksum(char sigGroupName[], long type, long disturbanceMode, long disturbanceCount, long disturbanceValue); // form 3
```

## Description

This function modifies the checksum. Different fault injections are possible.This function influences a simulation node with an assigned CANoe interaction layer.

## Parameters

| Name | Type | Description |
|---|---|---|
| aMessage |  | Message or PDU that should be modified. |
| aMsgName |  | Name of the message or PDU that should be modified. Supported qualification patterns for form 2: [DBName::][NodeName::]aMessageName |
| aSigGroupName |  | Some systems assign a checksum to a signal group. When specifying the signal group you can apply the disturbance to a dedicated signal group within a message or PDU. Use an empty character array if the checksum of the whole message or PDU should be affected. Supported qualification patterns for form 3: [DBName::][NodeName::][MessageName::]aSignalgroupName |
| checksumType |  | The possible values are described in the corresponding OEM Package manual. |
| 0 | Value | The disturbance uses the value in disturbanceValue as checksum. |
| 1 | Freeze | The current checksum value is transmitted. |
| 2 | Random | A random value is transmitted as checksum. |
| 3 | Offset | The checksum is incremented with the value in disturbanceValue. |
| -1 |  | Infinite. |
| 0 |  | Stops the disturbance, e.g.a infinite disturbance. |
| n |  | Number of disturbances. |
| disturbanceValue |  | This value is used in combination with the disturbanceMode. |

## Example

```c
// Disturbs the Checksum of a specific PDU, disturbance pattern: 20x fix value

variables {
  long checksumType = 0; // The possible values are described in the corresponding OEM Package manual.
  long disturbanceMode = 0; // The disturbance uses the value in disturbanceValue as checksum.
  long disturbanceCount = 20;
  long disturbanceValue = 10;
}

on key 'a' {
  ILNodeDisturbChecksum("PDU_A", "", checksumType, disturbanceMode, disturbanceCount, disturbanceValue);
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
