# SetControlVisibility

> Category: `Other` | Type: `function`

## Syntax

```c
void SetControlVisibility(char[] panel, char[] control, long visible);
```

## Description

Sets the visibility of panel elements.

The panel is accessed by its individual panel name that is entered in the Panel Designer/Panel Editor.

## Return Values

—

## Example

```c
// Set the visibility for a specific control of a panel
SetControlVisibility("motor", "PedalPos", 1);
// All controls of the panel are set to not visible
SetControlVisibility("motor", "", 0);
// All controls of all panels are set to visible
SetControlVisibility("", "", 1);
```

## Availability

| Since Version |
|---|
