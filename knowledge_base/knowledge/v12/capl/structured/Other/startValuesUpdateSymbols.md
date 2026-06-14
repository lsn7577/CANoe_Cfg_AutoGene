# startValuesUpdateSymbols

> Category: `Other` | Type: `function`

## Syntax

```c
void startValuesUpdateSymbols(char groupName[]);
```

## Description

Sets the variables/signals contained in a specific group to their individual start values in the CANoe Start Value Window.

## Return Values

—

## Example

```c
on key '3'
{
startValuesUpdateSymbols("Start values group2");
}

on key '4'
{
startValuesUpdateSymbols("");
}
```

## Availability

| Since Version |
|---|
