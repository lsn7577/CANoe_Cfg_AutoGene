# Iso11783IL_TIMSetSupportedFacility

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetSupportedFacility(char functionFacilityName[], long value); // form 1
long Iso11783IL_TIMSetSupportedFacility(dbNode server , char functionFacilityName[], long value); // form 2
```

## Description

The function sets a facility of a TIM function in a TIM server.

By means of this function you can define all possible TIM functions supported by the TIM server.

If least one facility of a function is set then the function is listed in the TIM_FunctionsSupportResponse message. By default the other facilities of the function are set to value 3 (not available).

You can use Iso11783IL_TIMResetAllSupportedFunctions to remove all functions and all of their facilities. Then they are no longer listed in the TIM_FunctionsSupportResponse message.

## Parameters

| Name | Description |
|---|---|
| functionFacilityName | Name if the function facility. auxiliaryValve<N>State (N = 1..32) auxiliaryValve<N>Flow (N = 1..32) frontPTODisengagement frontPTOEngagementCounterClockwise frontPTOEngagementClockwise frontPTOSpeedCounterClockwise frontPTOSpeedClockwise rearPTODisengagement rearPTOEngagementCounterClockwise rearPTOEngagementClockwise rearPTOSpeedCounterClockwise rearPTOSpeedClockwise frontHitchMotion frontHitchPosition rearHitchMotion rearHitchPosition vehicleSpeedForward vehicleSpeedReverse vehicleSpeedStartMotion vehicleSpeedStopMotion vehicleSpeedForwardDirection vehicleSpeedReverseDirection vehicleSpeedChangeOfDirection externalGuidanceCurvature |
| Value | Meaning |
| 0 | Server does not support this facility |
| 1 | Server supports this facility |
| 2 | Reserved |
| 3 | The facility was not defined when the server was built |
| server | TIM server node. |

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
