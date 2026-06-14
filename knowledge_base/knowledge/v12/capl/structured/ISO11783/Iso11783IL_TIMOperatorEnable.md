# Iso11783IL_TIMOperatorEnable

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_TIMOperatorEnable(dbNode server); // form 1
```

## Description

This function enables the TIM client function(s) after the client is successfully authenticated.

By calling this function the state of the TIM client (which is transmitted by TIM_ClientStatus_Msg) is set to Automation enabled.

If you previously have assigned one or more functions (via Iso11783IL_TIMAssignFunction), then the message TIM_FunctionsAssignmentRequest is sent to the TIM server.

You can also call Iso11783IL_TIMAssignFunction after calling this function, which leads to a transmission of the TIM_FunctionsAssignmentRequest message at once.

After receiving a successful TIM_FunctionsAssignmentResponse of the TIM server, the TIM client starts sending value request messages with value Ready to control to the server and waits for an operator acknowledgment.

This function is only successful if the TIM client is in Automaton ready to enable state.

## Return Values

0: Property has been set successfully

## Availability

| Since Version |
|---|
