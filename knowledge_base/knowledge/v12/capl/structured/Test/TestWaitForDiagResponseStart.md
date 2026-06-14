# TestWaitForDiagResponseStart

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagResponseStart (diagRequest request, dword timeout);
```

## Description

Waits for the arrival of the response to a sent request, e.g. the so-called "First Frame" in ISO TP transmissions. One way this function might be triggered is by Diag_FirstFrameInd() at the CAPL Callback Interface, but only if this has been implemented suitably. When other protocols or interfaces are used this call might be omitted. Then the function rolls back after the response has been fully received.

## Return Values

<0: An internal error occurred, e.g. a faulty configuration of the Diagnostic Layer.

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

| Since Version |
|---|
