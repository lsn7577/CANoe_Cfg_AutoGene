# TestWaitForNextCall

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
long TestWaitForNextCall(providedMethodRef * method, dword timeoutMs); // form 1
long TestWaitForNextCall(distObjMethodRef * method, dword timeoutMs); // form 2
```

## Description

Waits for the next call of the method at the simulated provider. You may use a specific endpoint combination to wait for the call of a specific consumer or the combination [all,<provider>] to wait for a call of any consumer.

You can get information about the call with the CurrentCCO property or through the LatestCall value (both at the method endpoint).

## Parameters

| Name | Description |
|---|---|
| method | Method provider where the call is awaited. |
| timeoutMS | Timeout in milliseconds. |

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
