# TestIso11783IL_OPLock

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPLock( dbNode node, dword lock, dword maskID, dword timeout );
```

## Description

The function locks the screen updates on the Virtual Terminal. A Lock command is sent to the Virtual Terminal.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
