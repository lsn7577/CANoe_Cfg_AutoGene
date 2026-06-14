# ClockControlReset

> Category: `Other` | Type: `function`

## Syntax

```c
void ClockControlReset(char[] panel, char[] control);
```

## Description

Resets the Clock Control designed as stop watch with the Panel Designer (setting Mode = StopWatch).

The displayed time is reset to 00:00:00 or 00:00 depending on the Panel Designer setting Display Seconds.

The stop watch cannot be reset when it is already running.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Return Values

—

## Example

```c
// Reset the clock control designed as stop watch.
on key 'a'
{
ClockControlReset("ClockControl", "StoppWatch");
}
```

## Availability

| Since Version |
|---|
