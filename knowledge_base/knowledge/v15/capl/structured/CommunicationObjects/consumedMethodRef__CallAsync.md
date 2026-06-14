# consumedMethodRef::CallAsync

> Category: `CommunicationObjects` | Type: `method`

## Syntax

```c
callcontext <MethodType> consumedMethodRef::CallAsync(params ...); // form 1
void consumedMethodRef::CallAsync(params ..., Callback); // form 2
```

## Description

Calls the method from the specified consumer at the specified provider. The function call is made asynchronously, i.e. the call does not wait for the function to be called and the return to be received. In test procedures, you can wait for the answer with TestWaitForAnswer; in simulation programs, you can use the handler on fct_Returned. In form 2, the callback function is called when the return is received.

## Example

```c
callContext MirrorAdjustment.Adjust cco;
int waitResult;
cco = MirrorAdjustment.consumerSide[CANoe,LeftMirror].Adjust.CallAsync(50, 0);
waitResult = testWaitForAnswer(cco, 500);
if (waitResult == 1 && cco.Result == Mirrors::AdjustResult::OK)
{
  testStepPass("AdjustCall", "Call returned with OK");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
