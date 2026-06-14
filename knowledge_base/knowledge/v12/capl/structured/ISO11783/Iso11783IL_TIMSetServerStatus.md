# Iso11783IL_TIMSetServerStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetServerStatus(dword cycleTime); // form 1
```

## Description

Forms (1, 3): This function changes the cycle time of the TIM_ServerStatus_Msg message. The content of TIM_ServerStatus_Msg message stays unchanged.

Forms (2, 4): This function changes the content and cycle time of the TIM_ServerStatus_Msg message.

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
