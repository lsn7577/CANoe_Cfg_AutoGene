# Iso11783IL_TIMSetRequiredFacility

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetRequiredFacility(char facilityName[], long value); // form 1
long Iso11783IL_TIMSetRequiredFacility(dbNode client, char facilityName[], long value); // form 2
```

## Description

Specifies if a TIM function facility is required by the TIM client or not.

After receiving the Functions Support Response message of the server the client checks if all defined required function facilities are supported by the server. If there are facilities that are not supported, the TIM Client terminates the automation.

You can use Iso11783IL_TIMResetAllRequiredFunctions to empty the list of necessary facilities.

## Parameters

| Name | Description |
|---|---|
| facilityName | Name if the TIM function facility. auxiliaryValve<N>State (N = 1..32) auxiliaryValve<N>Flow (N = 1..32) frontPTODisengagement frontPTOEngagementCounterClockwise frontPTOEngagementClockwise frontPTOSpeedCounterClockwise frontPTOSpeedClockwise rearPTODisengagement rearPTOEngagementCounterClockwise rearPTOEngagementClockwise rearPTOSpeedCounterClockwise rearPTOSpeedClockwise frontHitchMotion frontHitchPosition rearHitchMotion rearHitchPosition vehicleSpeedForward vehicleSpeedReverse vehicleSpeedStartMotion vehicleSpeedStopMotion vehicleSpeedForwardDirection vehicleSpeedReverseDirection vehicleSpeedChangeOfDirection externalGuidanceCurvature |
| Value | Description |
| 0 | Facility is not required by the TIM client. |
| 1 | Facility is required by the TIM client. |
| client | TIM client node. |

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
