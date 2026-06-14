# SetControlColors

> Category: `Other` | Type: `function`

## Syntax

```c
void SetControlColors(char[] panel, char[] control, long backcolor, long textcolor);
```

## Description

Sets the background and text color of panel elements.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Return Values

—

## Example

```c
//Set the background and text color for a specific control of a panel
SetControlColors("motor", "PedalPos", MakeRGB(255,0,0), MakeRGB(0,0,255));
//All controls of the panel are set to the same background and text color
SetControlColors("motor", "", MakeRGB(255,0,0), MakeRGB(0,0,255));
//All controls of all panels are set to the same background and text color
SetControlColors("", "", MakeRGB(255,0,0), MakeRGB(0,0,255));
```

## Availability

| Since Version |
|---|
