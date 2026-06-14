# ChkStart_SignalCycleTimeViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_SignalCycleTimeViolation (Signal ObservedSignal, duration MinCycleTime, duration MaxCycleTime);
```

## Description

Checks the occurrences of a signal.

An event will be generated, if the time between two consecutive signal occurrences is out of the specified range.

Limit set to 0 is considered as "cycle time is undefined"; at least one limit has to be more than 0.

## Example

```c
...
dword checkId;
// Create and start the check for LIN wake-up request
checkId = ChkStart_SignalCycleTimeViolation(Motor1State_Cycl::Motor1Temp,
            29,   // min. cycle time in ms
            32,   // max cycle time in ms
            "SigCycleTimeCallback"); 
...
// CAPL callback for violation notification
void SigCycleTimeCallback (dword aCheckId)
{
   ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
