# consumedMethodRef::CallAsyncPhys

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
callcontext <MethodType> consumedMethodRef::CallAsync_Phys(params ...); // form 1
```

## Description

Calls the method from the specified consumer at the specified provider. The function call is made asynchronously, i.e. the call does not wait for the function to be called and the return to be received. In test procedures, you can wait for the answer with TestWaitForAnswer; in simulation programs, you can use the handler on fctReturned. In form 2, the callback function is called when the return is received.

## Return Values

A call context object for the call. You can e.g. use it to wait for the return or to retrieve a unique request ID which you can match in a on fctReturned handler.

## Example

```c
callContext MirrorAdjustment.Adjust cco;
int waitResult;
cco = MirrorAdjustment.consumerSide[CANoe,LeftMirror].Adjust.CallAsync_Phys(50, 0);
waitResult = testWaitForAnswer(cco, 500);
if (waitResult == 1 && cco.Result == Mirrors::AdjustResult::OK)
{
  testStepPass("AdjustCall", "Call returned with OK");
}
```

## Availability

| Since Version |
|---|
