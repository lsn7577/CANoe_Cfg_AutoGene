# StmQuery_Valid

> Category: `Test` | Type: `function`

## Syntax

```c
long StmQuery_Valid (Check aStimulusId)
stimulus.QueryValid()
```

## Description

Examines whether a stimulus with particular Id is valid.

## Return Values

= 0: Refer the query error codes

## Example

```c
double result;
dword stmId;
stmId = StmCreate_Toggle(Velocity, 60, 80, 100);
// ... execute test sequence
result = StmQuery_Valid(stmId);
```

## Availability

| Since Version |
|---|
