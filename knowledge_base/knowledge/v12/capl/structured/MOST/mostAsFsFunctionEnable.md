# mostAsFsFunctionEnable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsFsFunctionEnable(long functionId, long opTypes)
```

## Description

mostAsFsFunctionEnable() registers a function and its operations with the function service. The service must have been previously enabled for the function block with mostAsFsEnable.

The second option registers a function with the notification service simultaneously. For this to be achieved, the function must be of the "Property" type and the notification service of the function block must have been previously enabled with mostAsNtfEnable.

Database support:

The special value functionID=-1 triggers the execution of the CAPL function for all MOST functions and operations of the function block from the function catalog.

## Return Values

See error codes

## Availability

| Since Version |
|---|
