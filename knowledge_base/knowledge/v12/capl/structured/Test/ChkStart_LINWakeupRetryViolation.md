# ChkStart_LINWakeupRetryViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkStart_LINWakeupRetryViolation (duration TimeoutAfterWakeup, duration TimeoutAfterThreeWakeups, float Tolerance, dword MaxRetryNum, char[] CaplCallback);
```

## Description

Checks number of LIN wake-up signals and the time between them.

An event will be generated, if

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Parameters

| Name | Description |
|---|---|
| 0 | Timeout between two consecutive retransmissions shall not be checked |
| >0 | Timeout between two consecutive retransmissions |

## Example

```c
...
dword checkId;
ChkConfig_SetPrecision(3); // set precision to ms
// Create and start the check for LIN Wake-Up signals
// Parameters to validate: Timeout between two wake-up signals – 150 ms,
// Timeout after each three wake-up signals – 1.5 sec, Allowed tolerance 2%, maximum 
// expected number of retransmitted Wake-Up signals - 4
checkId = ChkStart_LINWakeupRetryViolation (150, 1500, 2, 4, " LINWakeupRetryCallback"); 
...
// CAPL callback for violation notification
void LINWakeupRetryCallback (dword aCheckId)
{
ChkQuery_EventStatusToWrite(aCheckId);
}
```

## Availability

| Since Version |
|---|
