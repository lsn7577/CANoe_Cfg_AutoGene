# callcontext::ReleaseHandle

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void callContext::ReleaseHandle(long handle)
```

## Description

Releases a permanent handle for a call context. You need a permanent handle if you want to keep a call alive for a longer time, e.g. if you wish to store several call contexts in a (associative) array. You also need a permanent handle if you want to pass the call context e.g. to a CAPL DLL.

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
