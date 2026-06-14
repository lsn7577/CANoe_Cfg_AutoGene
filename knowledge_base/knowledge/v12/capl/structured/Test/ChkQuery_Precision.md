# ChkQuery_Precision

> Category: `Test` | Type: `function`

## Syntax

```c
double ChkQuery_Precision (dword aCheckId);
check.QueryPrecision();
```

## Description

Returns a factor that can be multiplied with the return value of the statistical queries to convert the time stamp to the standard unit milliseconds.

## Return Values

double: 100 to 10-6

## Example

```c
double result;
dword checkId;
checkId = ChkStart_MsgRelCycleTimeViolation(VehicleMotion, 0.9, 1.1);
// ... execute test sequence
result = ChkQuery_Precision(checkId);
```

## Availability

| Since Version |
|---|
