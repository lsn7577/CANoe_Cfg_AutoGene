# TestIso11783IL_PDDSetLogTrigger

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_PDDSetLogTrigger( dbNode node, dword command, ulong ddi, ulong elNum, ulong value );
```

## Description

A measurement command can be executed with this function. It can be used in the callback function Iso11783IL_PDDOnDefaultLogRequest to activate the default logging.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
