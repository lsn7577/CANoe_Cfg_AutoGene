# ChkQuery_StatMaxValidResponseTime

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_StatMaxValidResponseTime (dword aCheckId);
check.QueryStatMaxValidResponseTime();
```

## Description

Returns the longest time lag between the request and corresponding response message that occurred during the current observation period. Only those requests that were resolved within the specified maximum response time are taken into consideration here.

## Return Values

< 0: Refer the query error codes.

## Availability

| Since Version |
|---|
