# CreateGlobalMarker

> Category: `Other` | Type: `function`

## Syntax

```c
long createGlobalMarker (char markerName[], char makerDesc []);
```

## Description

Sets a marker in CANoe Trace Window, Graphics Window and State Tracker. The set marker can be displayed with the shortcut menu Show in the marker bar of these windows.

## Return Values

—

## Example

```c
on key 'a'
// sets a marker by pressing key <a>
{
  createGlobalMarker("speed", "speedDesc");
}
```

## Availability

| Since Version |
|---|
