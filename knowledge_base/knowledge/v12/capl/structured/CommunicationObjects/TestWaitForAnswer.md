# TestWaitForAnswer

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForAnswer(callContext cco, dword timeoutMs)
```

## Description

Waits for the answer to a method call. The call must have been created through consumedMethodRef::CallAsync on a consumed method.

If the wait is successful, the call context properties for the return value and the out parameters can be read.

## Return Values

-2: Resume due to constraint violation

## Example

```c
long ret;
callContext MirrorAdjustment.Adjust cco;

cco = MirrorAdjustment[0,0].Adjust.CallAsync(50, 0);
ret = TestWaitForAnswer(cco, 300);
if (ret == 1)
{
  write("Call result: %d", cco.Result);
}
```

## Availability

| Since Version |
|---|
