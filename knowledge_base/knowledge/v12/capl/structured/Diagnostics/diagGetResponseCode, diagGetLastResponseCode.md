# diagGetResponseCode, diagGetLastResponseCode

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagGetResponseCode (diagResponse resp);
```

## Description

Returns the code of the specified response or last received response (for the specified request).

## Return Values

-1: The response was positive, i.e. there is no error code.

## Availability

| Since Version |
|---|
