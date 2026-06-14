# ClockControlStart

> Category: `Other` | Type: `function`

## Syntax

```c
void ClockControlStart(char[] panel, char[] control);
```

## Description

Starts the Clock Control designed as stop watch in the Panel Designer (setting Mode = StopWatch).

The stop watch starts with 00:00:00 or 00:00 depending on the Panel Designer setting Display Seconds. The start time cannot be changed.

The stop watch is updated every second.

The stop watch cannot be started when it is already running.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Return Values

—

## Example

```c
// Start the clock control designed as stop watch.
on key 'a'
{
ClockControlStart("ClockControl", "StoppWatch");
}
```

## Availability

| Since Version |
|---|
