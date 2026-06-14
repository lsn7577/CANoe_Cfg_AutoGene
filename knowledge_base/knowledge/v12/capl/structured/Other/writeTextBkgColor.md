# writeTextBkgColor

> Category: `Other` | Type: `function`

## Syntax

```c
void writeTextBkgColor(dword sink,dword red, dword green, dword blue)
```

## Description

Sets the color for text background of the specified page in the Write Window.

You can use the following constants for the target identifier:

In addition you can use one of the target identifiers returned by the function writeCreate.

The color settings have also an effect on the All page of the Write Window.

## Return Values

—

## Example

```c
WriteTextColor(0,255,0,0);
WriteLineEx(0,1,"This is red text");

WriteTextBkgColor(0,0,255,0);
WriteLineEx(0,1,"This is red text with green background");

WriteTextColor(0,0,0,0);
WriteTextBkgColor(0,255,255,255);
WriteLineEx(0,1,"This is black text with white background");
```

## Availability

| Since Version |
|---|
