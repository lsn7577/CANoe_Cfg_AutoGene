# Iso11783IL_TIMConnectSysVarToState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMConnectSysVarToState(dbNode counterpart, char[] sysVarNameWithPath); // form 1
```

## Description

Connects the state of a TIM client/server connection to a system variable.

You find the possible states in the tables of Client States (TIM Component - ISO11783) or Server States (TIM Component - ISO11783).

By means of the function you can wait for a specific state (e.g. using TestWaitForSignalMatch) and with Iso11783IL_TIMFreezeConnection you can stay in this state.

To release connection between the system variable and a state, just call the same method again, but with the empty string instead of the name of system variable.

## Return Values

0: Property has been set successfully

## Example

```c
Iso11783IL_TIMConnectSysVarToState(TIMClient, "sysvarTIMClientState");
```

## Availability

| Since Version |
|---|
