# traceSetEventColors

> Category: `Other` | Type: `function`

## Syntax

```c
long traceSetEventColors(message msg, dword font, dword bkgnd)
```

## Description

Sets the text and background color for displaying msg in the Trace Window. The makeRGB function can be used for the colors.

## Return Values

0: OK

## Example

```c
on message *
{
   traceSetEventColors(this, makeRGB(0x00, 0xFF, 0xFF), makeRGB(0x00, 0x00, 0x00));
   output(this);
}
on message *
{
   message * msg;
   msg = this;
   traceSetEventColors(msg, makeRGB(0x00, 0xFF, 0xFF), makeRGB(0x00, 0x00, 0x00));
   output(msg);
}
```

## Availability

| Since Version |
|---|
