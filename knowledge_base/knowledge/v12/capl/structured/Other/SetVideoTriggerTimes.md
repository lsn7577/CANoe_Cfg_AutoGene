# SetVideoTriggerTimes

> Category: `Other` | Type: `function`

## Syntax

```c
SetVideoTriggerTimes(char windowName[], dword preTriggerTime, dword postTriggerTime);
```

## Description

Sets the trigger times for a CANoe Video Window.

## Return Values

—

## Example

```c
// set trigger times for "VideoWindow"
SetVideoTriggerTimes("VideoWindow", 0, 2500);
```

## Availability

| Since Version |
|---|
