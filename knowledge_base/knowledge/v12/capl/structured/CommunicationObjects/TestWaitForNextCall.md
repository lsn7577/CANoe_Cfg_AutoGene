# TestWaitForNextCall

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForNextCall(providedMethodRef * method, dword timeoutMs)
```

## Description

Waits for the next call of the method at the simulated provider. You may use a specific endpoint combination to wait for the call of a specific consumer or the combination [all,<provider>] to wait for a call of any consumer.

You can get information about the call with the CurrentCCO property or through the LatestCall value (both at the method endpoint).

## Return Values

-2: Resume due to constraint violation

## Example

```c
long ret;
providedMethodRef MirrorAdjustment.Adjust method;

method = MirrorAdjustment.providerSide[all,LeftMirror].Adjust;
ret = TestWaitForNextCall(method, 200);
if (ret == 1)
{
  int x;
  x = method.CurrentCCO.deltaX;
}
```

## Availability

| Since Version |
|---|
