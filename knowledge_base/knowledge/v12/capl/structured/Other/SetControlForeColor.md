# SetControlForeColor

> Category: `Other` | Type: `function`

## Syntax

```c
void SetControlForeColor(char[] panel, char[] control, long color);
```

## Description

Sets the foreground color of panel elements.

The panel is accessed by its individual panel name that is entered in the Panel Designer/Panel Editor.

## Return Values

—

## Example

```c
// Set the foreground color for a specific control of a panel
SetControlForeColor("motor", "PedalPos", MakeRGB(255,0,0));
// All controls of the panel are set to the same foreground color
SetControlForeColor("motor", "", MakeRGB(255,0,0));
// All controls of all panels are set to the same foreground color
SetControlForeColor("", "", MakeRGB(255,0,0));
```

## Availability

| Since Version |
|---|
