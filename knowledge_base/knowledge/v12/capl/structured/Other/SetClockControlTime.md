# SetClockControlTime

> Category: `Other` | Type: `function`

## Syntax

```c
void SetClockControlTime(char[] panel, char[] control, int hours, int minutes, int seconds);
```

## Description

Sets the time of the Panel Designer Clock Control.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Return Values

—

## Example

```c
// Set the time in hours, minutes, seconds. It will be displayed '10:20:30'.
on key 'a'
{
SetClockControlTime("ClockControl1", "ClockCAPL", 10, 20, 30);
}
// Set the time in seconds. It will be displayed '01:00:00'.
on key 'b'
{
SetClockControlTime("ClockControl1", "ClockCAPL", 3600);
}
```

## Availability

| Since Version |
|---|
