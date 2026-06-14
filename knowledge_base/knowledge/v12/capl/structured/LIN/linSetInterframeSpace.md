# linSetInterframeSpace

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetInterframeSpace(dword bitTimes)
```

## Description

This function sets the minimum inter-frame space.

With this function it is possible to change the inter-frame space for all frames.

The inter-frame space is the time from the end of the frame until start of the next frame.

By default the minimum inter-frame space is 0.

If the LIN hardware is not in Master mode calling this function will have no effect.

If large inter-frame space is set, the schedule slots time may be affected.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 's'
{
if (linSetInterframeSpace (200) != 0)
{
// from now on inter-frame space is minimum 200 bit times 
...
}
}
```

## Availability

| Since Version |
|---|
