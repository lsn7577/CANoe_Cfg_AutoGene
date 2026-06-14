# ChkQuery_StatAvResponseTime

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkQuery_StatAvResponseTime (dword aCheckId);
check.QueryStatAvResponseTime();
```

## Description

Returns the average time lag between the request and corresponding response messages. Only those requests that were resolved within the specified maximum response time are taken into consideration here.

## Return Values

< 0: Refer the query error codes.

## Availability

| Since Version |
|---|
