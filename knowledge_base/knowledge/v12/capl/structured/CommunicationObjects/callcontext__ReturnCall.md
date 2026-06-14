# callcontext::ReturnCall

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void callContext::ReturnCall()
```

## Description

Returns the call immediately, sending an answer to the caller. Note that many function calls require an answer per protocol even if the function has neither a return value nor an out parameter.

Immediately means in effect after the current handler has been processed or when the current test procedures reaches a wait instruction, but at the same point of (simulation) time.

You can optionally set the return value (if the function does not return void).

This call is equivalent to callcontext::SetTimeToAnswer(0).

## Return Values

—

## Example

```c
on fctCalled MirrorAdjustment.providerSide[all,LeftMirror].Adjust
{
  // return the call always only after 2 other calls have been received
  const dword nrOfCalls = 3;
  long ccHandles[nrOfCalls];
  dword nextCallSlot = 0;
  dword nrOfCallsReceived = 0;

  this.Result = Mirrors::AdjustResult::OK;
  this.DeferAnswer();
  ccHandles[nextCallSlot] = this.CreatePermanentHandle();
  nextCallSlot = (nextCallSlot + 1) % nrOfCalls;

  if (++nrOfCallsReceived >= nrOfCalls)
  {
    callContext * cco;
    dword returnSlot;
    returnSlot = nrOfCallsReceived % nrOfCalls;
    cco = cco::FromHandle(ccHandles[returnSlot]);
    cco.ReturnCall();
    cco::ReleaseHandle(ccHandles[returnSlot]);
  }
}
```

## Availability

| Since Version |
|---|
