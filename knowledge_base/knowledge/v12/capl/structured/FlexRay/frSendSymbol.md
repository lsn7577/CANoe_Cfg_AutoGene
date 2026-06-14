# frSendSymbol

> Category: `FlexRay` | Type: `function`

## Syntax

```c
frSendSymbol( long <type>, long <param>, int channel );
```

## Description

This function sends an MTS symbol in the next possible symbol window if the Communication Controller is in normal mode (synchronized).

## Return Values

—

## Example

Example

This example sends a MTS symbol when a key is pressed in the next possible cycle.

```c
on key 'm'
{
   frSendSymbol(0 /* not used */, 0 /* not used */, %CHANNEL%);
}
```

## Availability

| Since Version |
|---|
