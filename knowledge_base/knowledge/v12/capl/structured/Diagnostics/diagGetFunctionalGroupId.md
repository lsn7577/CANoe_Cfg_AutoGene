# diagGetFunctionalGroupId

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
dword diagGetFunctionalGroupId ()
```

## Description

Determines the CAN ID on which functional requests are sent by the diagnostic tester.

If the functional group is not specified, the destination set with diagSetTarget is used.

## Return Values

CAN ID of the requests, or 0xFFFFFFFF if no functional group has been set.

## Availability

| Since Version |
|---|
