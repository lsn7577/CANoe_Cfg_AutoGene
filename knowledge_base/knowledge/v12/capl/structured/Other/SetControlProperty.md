# SetControlProperty

> Category: `Other` | Type: `function`

## Syntax

```c
void SetControlProperty(char[] panel, char[] control, char[] property, long value);
```

## Description

Sets a property of a Panel Editor ActiveX control.For OCX panels properties can also be set. Therefore the property must be defined as property to be set in the OCX INI file.

The panel is accessed by its individual panel name that is entered in the Panel Editor.

It is easier to access color properties by MakeRGB.

## Return Values

—

## Example

```c
SetControlProperty("Measurements", "StatusIndicator", "Caption", "running");
SetControlProperty("Measurements", "StatusIndicator", "BackColor", MakeRGB(0,145,255));
```

## Availability

| Since Version |
|---|
