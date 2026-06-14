# ChkQuery_NumTimedoutRequests

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_NumTimedoutRequests (dword aCheckId);
check.QueryNumTimedoutRequests();
```

## Description

Returns the number of requests within the current observation period for which no corresponding response message was observed during the specified timeout.

In the context of a method protocol check, an occurred timeout of tWaitForProcessing1 or tWaitForProcessing2 will also count that request to the number returned by this function, regardless whether the final "Result"/"ResultAck" or "Error"/"ErrorAck" response is observed within tMaxDuration or not.

## Return Values

< 0: Refer the query error codes.

## Availability

| Since Version |
|---|
