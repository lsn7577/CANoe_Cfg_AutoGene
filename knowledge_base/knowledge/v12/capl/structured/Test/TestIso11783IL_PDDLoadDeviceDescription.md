# TestIso11783IL_PDDLoadDeviceDescription

> Category: `Test` | Type: `function`

## Syntax

```c
long TestIso11783IL_PDDLoadDeviceDescription( dbNode node, char deviceCfgPath[] );
```

## Description

The function creates a process data dictionary from a machine configuration file (XML).

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Availability

| Since Version |
|---|
