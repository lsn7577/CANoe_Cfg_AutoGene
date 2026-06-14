# TestFRILEnableTimingImmed

> Category: `Test` | Type: `function`

## Syntax

```c
long TestFRILEnableTimingImmed (char pduName[], int enable);
```

## Description

Controls the immediate timing of PDUs. The immediate timing can be enabled/ disabled.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
int enable;
.....
If( stopImmedSending == 1 )
{
   enable = 0;
}
else
{
   enable = 1;
}
TestFRILEnableTimingImmed (pduXY, enable);
.....
```

## Availability

| Since Version |
|---|
