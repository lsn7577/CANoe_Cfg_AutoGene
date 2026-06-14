# TestIso11783IL_OPStoreVersion

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_OPStoreVersion( dbNode node, char versionName[] );
```

## Description

The function stores the current object pool on the Virtual Terminal. A Store Version command is sent to the Virtual Terminal.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
