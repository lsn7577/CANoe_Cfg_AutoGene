# callContext

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
callContext * <var>
```

## Description

Contains data of a function call, in particular the parameter values.

## Example

```c
variables
{
  callContext MirrorAdjustment.Adjust deferredAnswer;
}

on fctCalling MirrorAdjustment[all, LeftMirror].Adjust
{
  this.DeferAnswer();
  deferredAnswer = this;
}

on sysvar Panels::ReturnAnswer
{
  deferredAnswer.ReturnCall(Mirrors::AdjustResult::OK);
}
```

## Availability

| Since Version |
|---|

## Selectors

| Selector | Type | Access Limitation |
|---|---|---|
| State State of the call: eCALLSTATE_INITIAL: the call has not yet reached the provider eCALLSTATE_CALLED: the call has reached the provider, but the return has not yet reached the consumer eCALLSTATE_RETURNED: the return has reached the consumer eCALLSTATE_DISCARDED: the call context is invalid | enumeration | Read only |
| Side Shows where the call is currently being handled: eCOSIDE_CONSUMER: consumer side eCOSIDE_PROVIDER: provider side | enumeration | Read only |
| Consumer Name of the consumer which started the call. | char[] | Read only |
| Provider Name of the provider which is called. | char[] | Read only |
| CallTime Point of time (in simulation time, in nanoseconds) when the call was started (on consumer side) or the call reached the provider (on provider side). | int64 | Read only |
| ReturnTime Point of time (in simulation time, in nanoseconds) when the call was returned to the consumer (on provider side) or the return reached the consumer (on consumer side). | int64 | Read only |
| ReqID A request ID which identifies the call. Can be used to match replies to calls if several calls are waiting for a reply. The request ID is internal and not necessarily transmitted on the network. | int64 | Read only |
| <Parameter Name> Value of the named parameter. Note that parameters are not accessible or read-only depending on the side and state of the call, e.g. you cannot access out-parameters in state Initial and cannot change in-parameters in state Returned. | <data type of the parameter> | <depends on side and state> |
| Result Return value of the function (if the function return type is not void). | <data type of the return value> | <depends on side and state> |
