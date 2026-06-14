# Iso11783IL_TIMConnectSysVarToFunctionState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMConnectSysVarToFunctionState(dword functionID, char[] sysVarNameWithPath); // form 1
```

## Description

Connects the automation state of a TIM function to a system variable.

0

Automation unavailable

1

Automation not ready

2

Automation ready to enable

3

Automation enabled

4

Automation pending

5

Active, not limited

6

Active, limited high

7

Active, limited low

14

Non-recoverable fault

15

Not available (parameter not supported or not configured for TIM)

If this function is used by a TIM client the system variable only changes if the TIM function is assigned by the client.

To release connection between the system variable and the function, just call the same method again, but with the empty string instead of the name of system variable.

You can also use the callback function Iso11783IL_TIMOnFunctionStateChanged if you are interested in the state of a function.

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

## Return Values

0: Property has been set successfully

## Example

```c
Iso11783IL_TIMConnectSysVarToFunctionState(0, "sysvarAuxValve1State");
```

## Availability

| Since Version |
|---|
