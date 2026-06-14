# Iso11783IL_TIMFreezeConnection

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMFreezeConnection(dbNode counterpart, dword runToState); // form 1
```

## Description

After calling this function the TIM client or TIM server runs until the specified state is reached. In this state the node still sends the cyclic status messages.

You find the possible states in the tables of Client States (TIM Component - ISO11783) or Server States (TIM Component - ISO11783).

To continue the standard process you can call Iso11783IL_TIMContinueConnection.

For form 2, 4, 6 and 8 you can specify an additional system variable which is set to value 1 if the specified state is reached.

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
