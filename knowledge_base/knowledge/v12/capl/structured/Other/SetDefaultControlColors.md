# SetDefaultControlColors

> Category: `Other` | Type: `function`

## Syntax

```c
void SetDefaultControlColors(char[] panel, char[] control);
```

## Description

Sets back the background and text color of panel elements as defined in the Panel Designer.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Return Values

—

## Example

```c
//Set the default background and text color for a specific control of a panel.
SetDefaultControlColors("motor", "PedalPos");
//All controls of the panel are set to the default background and text color as defined in the Panel Designer.
SetDefaultControlColors("motor", "");
//All controls of all panels are set to the default background and text color as defined in the Panel Designer.
SetDefaultControlColors("", "");
```

## Availability

| Since Version |
|---|
