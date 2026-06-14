# TestWaitForDiagRequestSent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagRequestSent (diagRequest request, dword timeout);
```

## Description

Waits until the previously sent request has been sent to the ECU. This might be triggered by a call of the function Diag_DataCon() at the CAPL Callback Interface.

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
// waits until request is completely sent
if (TestWaitForDiagRequestSent(req, 2000)== 1)
  TestStepPass("Request was sent successfully!");
else
  TestStepFail("Request could not be sent!");
TestWaitForDiagResponse(req, 2000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | — | — | — | 1.0 |
| Restricted To | — | Test mode | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | — | ✔ | — | N/A | — | N/A |
| 64-Bit | — | ✔ | — | — | — | N/A |
