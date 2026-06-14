# startValuesUpdateList

> Category: `Other` | Type: `function`

## Syntax

```c
void startValuesUpdateList(); // form 1
```

## Description

Sets the start values of variables/signals to the currently measured values in the CANoe Start Value Window.

## Return Values

—

## Example

```c
on key '1'
{
  startValuesUpdateList("Start values group1");
}

on key '2'
{
  startValuesUpdateList();
}

on key '3'
{
  startValuesUpdateList(""); // corresponds to startValuesUpdateList();
}

on key '4'
{
  startValuesUpdateList("Start values group1", 1);
}
```

## Availability

| Since Version |
|---|
