# ClockControlStop

> Category: `Other` | Type: `function`

## Syntax

```c
void ClockControlStop(char[] panel, char[] control);
```

## Description

Stops the Clock Control designed as stop watch with the Panel Designer (setting Mode = StopWatch).

The displayed time stays unchanged unless the user starts the stop watch again or resets it.

If the stop watch is started again without resetting it, the start time is the current displayed time (not zero).

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Return Values

—

## Example

```c
// Stop the clock control designed as stop watch.
on key 'a'
{
ClockControlStop("ClockControl", "StoppWatch");
}
```

## Availability

| Since Version |
|---|
