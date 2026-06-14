# SetControlBackColor

> Category: `Other` | Type: `function`

## Syntax

```c
void SetControlBackColor(char[] panel, char[] control, long color);
```

## Description

Sets the background color of panel elements.

The panel is accessed by its individual panel name that is entered in the Panel Designer/Panel Editor.

## Return Values

—

## Example

```c
// Set the background color for a specific control of a panel
SetControlBackColor("motor", "PedalPos", MakeRGB(255,0,0));
// All controls of the panel are set to the same background color
SetControlBackColor("motor", "", MakeRGB(255,0,0));
// All controls of all panels are set to the same background color
SetControlBackColor("", "", MakeRGB(255,0,0));
```

## Availability

| Since Version |
|---|
