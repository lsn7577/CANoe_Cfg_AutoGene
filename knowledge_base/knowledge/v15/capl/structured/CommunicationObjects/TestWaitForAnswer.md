# TestWaitForAnswer

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForAnswer(callContext cco, dword timeoutMs);
```

## Description

Waits for the answer to a method call. The call must have been created through consumedMethodRef::CallAsync on a consumed method.

If the wait is successful, the call context properties for the return value and the out parameters can be read.

## Parameters

| Name | Description |
|---|---|
| cco | Call context for a call. |
| timeoutMS | Timeout in milliseconds. |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 12.0 | 13.0 | 15 | 14 | 4.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
