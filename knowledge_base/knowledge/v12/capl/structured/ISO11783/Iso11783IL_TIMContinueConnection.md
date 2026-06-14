# Iso11783IL_TIMContinueConnection

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMContinueConnection(dbNode counterpart); // form 1
```

## Description

Continues a connection which has been frozen by Iso11783IL_TIMFreezeConnection.

Form 1, 3, 5, and 7 continues the state of the currently frozen connection by execution the action of this state.

Form 2, 4, 6 and 8 continues with the specified state and executes the action of this state.

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
