# TestWaitForDiagRequestSent

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagRequestSent (diagRequest request, dword timeout);
```

## Description

Waits until the previously sent request has been sent to the ECU. This might be triggered by a call of the function Diag_DataCon() at the CAPL Callback Interface.

## Return Values

<0: An internal error occurred, e.g. a faulty configuration of the Diagnostic Layer.

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

| Since Version |
|---|
