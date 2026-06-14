# TestWaitForDiagResponseStart

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagResponseStart (diagRequest request, dword timeout);
long TestWaitForDiagResponseStart (dword timeout);
```

## Description

Waits for the arrival of the response to a sent request, e.g. the so-called "First Frame" in ISO TP transmissions. One way this function might be triggered is by Diag_FirstFrameInd() at the CAPL Callback Interface, but only if this has been implemented suitably. When other protocols or interfaces are used this call might be omitted. Then the function rolls back after the response has been fully received.

## Parameters

| Name | Description |
|---|---|
| request | Sent request |
| timeout [ms] | Maximum wait time |

## Example

```c
DiagRequest SerialNumber_Read req;
long result;

DiagSetTarget("Door");
req.SendRequest();
// waits for the start of the response reception
if (TestWaitForDiagResponseStart(req, 2000)== 1)
   TestStepPass("Starting response reception!!");
else
   TestStepFail("No response!");
TestWaitForDiagResponse(req, 2000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | — | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
