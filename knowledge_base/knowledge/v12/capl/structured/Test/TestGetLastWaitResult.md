# TestGetLastWaitResult

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetLastWaitResult();
```

## Description

Makes available the last occurred return value of a TestWait instruction once again.

## Return Values

See TestWait instructions

## Example

```c
TestWaitForTimeout(100);
Write("Waiting Result = %d", TestGetLastWaitResult());
```

## Availability

| Since Version |
|---|
