# TestFRILEnableTimingEvtTrg

> Category: `Test` | Type: `function`

## Syntax

```c
long TestFRILEnableTimingEvtTrg(char pduName[], int enable);
```

## Description

Controls the event triggered timing of PDUs. The event triggered timing can be enabled/ disabled.

This function influences a simulation node with an assigned CANoe Interaction Layer.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
int enable;
.....
If( stopEvtSending == 1 )
{
   enable = 0;
}
else
{
   enable = 1;
}
TestFRILEnableTimingEvtTrg (pduXY, enable);
.....
```

## Availability

| Since Version |
|---|
