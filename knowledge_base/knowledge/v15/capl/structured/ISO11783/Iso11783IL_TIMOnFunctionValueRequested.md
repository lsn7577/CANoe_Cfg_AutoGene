# Iso11783IL_TIMOnFunctionValueRequested

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void Iso11783IL_TIMOnFunctionValueRequested(dword functionID, dword requestedRawValue, dword& calculatedRawValue, dword& calculcatedExitReasonCode dword& calculatedAutomationStatus )
```

## Description

This callback function is called if a function request message is received for an assigned function.

The Interaction Layer checks the requested value and calls this callback with the value and the exit reason code the IL would use. You can change the value and the exit reason code in the callback.

## Parameters

| Name | Description |
|---|---|
| Function ID | Description |
| 1-32 (1h-20h) | Auxiliary Value 1 – 32 |
| 64 (40h) | Front PTO |
| 65 (41h) | Rear PTO |
| 66 (42h) | Front hitch |
| 67 (43h) | Rear hitch |
| 68 (44h) | Vehicle speed |
| 70 (46h) | External guidance |
| requestedRawValue | Value which is requested by the TIM Client. |
| calculatedRawValue | The interaction layer suggest using this function value. If you modify this value in the callback the modified value is the new function value. |
| calculcatedExitReasonCode | The interaction layer suggest using this exit reason code value in the responding function status message. If modify this value in the callback the modified exit reason code is used in the function status message. |
| calculatedAutomationStatus | The interaction layer suggest using this automation status value in the responding function status message. If modify this value in the callback the modified automation status is used in the function status message. |

## Return Values

—

## Example

```c
void Iso11783IL_TIMOnFunctionValueRequested (
  dword fctID,
  dword requestedRawValue,
  dword& calculatedRawValue,
  dword& calculcatedExitReasonCode,
  dword& calculcatedAutomationStatus)
{
  switch (fctID)
  {
   case cRearPTO:
      if ((calculatedRawValue >= 0x0001) && (calculatedRawValue <= 0x7D7F)) // speed counter-clockwise
      {
        if (calculatedRawValue < 0x1FC0)
        {
          calculatedRawValue = 0x1FC0; // -3000 1/min
          calculcatedExitReasonCode = cReasonRemoteCommandOutOfRange;
          calculcatedAutomationStatus = cActiveLimitedLow;
        }
      }
      else if ((calculatedRawValue >= 0x7D81) && (calculatedRawValue <= 0xFAFF)) // speed clockwise
      {
        if (calculatedRawValue > 0xDB40) // 3000 1/min
        {
          calculatedRawValue = 0xDB40;
          calculcatedExitReasonCode = cReasonRemoteCommandOutOfRange;
          calculcatedAutomationStatus = cActiveLimitedHigh;
        }
      }
      break;
    case cVehicleSpeed:
      if ((calculatedRawValue >= 0x0001) && (calculatedRawValue <= 0x7D7F)) // reverse speed
      {
        if (calculatedRawValue < 0x1BD8)
      {
        calculatedRawValue = 0x1BD8;
        calculcatedExitReasonCode = cReasonRemoteCommandOutOfRange;
        calculcatedAutomationStatus = cActiveLimitedLow;
      }
    }
    else if ((calculatedRawValue >= 0x7D81) && (calculatedRawValue <= 0xFAFF)) // forward speed
    {
      if (calculatedRawValue > 0xDF25)
      {
        calculatedRawValue = 0xDF25; // 25 m/s
        calculcatedExitReasonCode = cReasonRemoteCommandOutOfRange;
        calculcatedAutomationStatus = cActiveLimitedHigh;
      }
    }
    break;
  default:
    break;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | — |
| Restricted To | — | ISO11783 | ISO11783 | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | — | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | — | — | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
