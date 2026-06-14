# Iso11783IL_TIMSetClientStatus

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMSetClientStatus(dbNode server, dword cycleTime); // form 1
```

## Description

Forms (1,3): This function changes the cycle time of the TIM_ClientStatus_Msg message. The content of TIM_ClientStatus_Msg message stays unchanged.

Forms (2,4): This function changes the content and cycle time of the TIM_ClientStatus_Msg message.

## Return Values

0: Function has been executed successfully

## Availability

| Since Version |
|---|
