# DeleteControlContent

> Category: `Other` | Type: `function`

## Syntax

```c
void DeleteControlContent(char[] panel, char[] control);
```

## Description

Deletes the content of the Panel Designer CAPL Output View control.

The panel is accessed by its individual panel name that is entered in the Panel Designer.

## Return Values

—

## Example

```c
// Deletes the contents of a specific CAPL Output View control in the panel motor
DeleteControlContent(„motor“, „Outputview“);
// Deletes the contents of all CAPL Output View controls in the panel motor
DeleteControlContent(„motor“, „“);
// Deletes the contents of all CAPL Output View controls in all panels
DeleteControlContent(„“, „“);
```

## Availability

| Since Version |
|---|
