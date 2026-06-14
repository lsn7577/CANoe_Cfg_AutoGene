# callcontext::SetTimeToAnswer

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long callContext::SetTimeToAnswer(dword timeMs)
```

## Description

Tells the simulation when it shall return the answer for the call. The answer will be returned after the given time.

Note that you can also use the AutoAnswerTimeNS property of a method provider endpoint to set the answer delay for all following calls.

## Return Values

—

## Example

```c
on fctCalled MirrorAdjustment.providerSide[all,LeftMirror].Adjust
{
  this.Result = Mirrors::AdjustResult::OK;
  // return the call after 10 ms
  this.SetTimeToAnswer(10);
}
```

## Availability

| Since Version |
|---|
