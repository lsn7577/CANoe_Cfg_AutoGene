# graphicsWindowPause

> Category: `Other` | Type: `function`

## Syntax

```c
void graphicsWindowPause(char[] windowName, byte active);
```

## Description

Pauses and resumes a CANoe Graphics Window.

## Return Values

—

## Example

```c
//Pause the Graphics Window
graphicsWindowPause("Graphics", 1);

//Fit the y axis so that all values are visible
graphicsWindowFit("Graphics", 2);
```

## Availability

| Since Version |
|---|
