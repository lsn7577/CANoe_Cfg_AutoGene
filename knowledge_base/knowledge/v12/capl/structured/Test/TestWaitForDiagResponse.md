# TestWaitForDiagResponse

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForDiagResponse (diagRequest request, dword timeout); // form 1
```

## Description

Waits for the arrival of the response to the given request.

Please note that in case no response is received, it depends on the transport layer settings (e.g. P2 timing) whether the function returns with a timeout or an internal error.

Before calling the function TestWaitForDiagResponse, make sure the request has already completely been sent using the function TestWaitForDiagRequestSent().

The function will return immediately after a positive or negative response - other than "responsePending" - was received within the configured protocol (P2/P2*) timings.

Intermediate "responsePending" NRCs from the target ECU will automatically prolong the wait timer of the tester in P2* increments until maximally <timeout> [ms]. If by then no response has been received from the ECU target, the function will return with value =0 (timeout reached).

In case the tester node implements a "CAPL callback interface for diagnostics" (CCI), but has no further provisions to handle NRCs on its own right, the behaviour is equivalent to the one described above (automated "responsePending" handling).

If the tester implements a CCI and handles "responsePending" messages by itself - calling DiagSetP2Extended(-1) beforehand on the CCI - then this function will also treat "responsePending" as a regular negative response code and will return immediately after having received such a negative response.

Using the syntax with diagRequest object (form 1), the check on P2 or P2 extended does not take into account, whether the response fits to the request or not.

If a response (whether fitting or not) was received within P2 or P2 extended, the TP timings are treated as correct by the function and the further evaluation is executed on diagnostic layer.

If P2 or P2 extended is violated, the function returns with a negative return value, i.e. the timeout parameter value gets irrelevant and it doesn't matter if a fitting response was received during the timeout or not.

The diagnostic layer gets only responses for fitting requests, i.e.:

Therefore, the function waits until the timeout, which was passed as a parameter, when it receives an unfitting response.

## Return Values

<0: An internal error occurred, e.g. a protocol error or a faulty configuration of the diagnostic layer.

## Availability

| Since Version |
|---|
