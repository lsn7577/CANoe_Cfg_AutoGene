# linSetGlobalInterByteSpace

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetGlobalInterByteSpace(dword sixteenthBits)
```

## Description

With this function it is possible to change the inter-byte space for all frame responses. Inter-byte space is the period between the end of the stop bit of the preceding byte and the start bit of the following byte.

By default the inter-byte space is 0.

This function affects only frames published by the modeled LIN node(s), i.e. frames sent not by external hardware.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

Example

```c
on key 's'
{
if ( linSetGlobalInterByteSpace(16) != 0)
{
// from now on the inter-byte space in all frame 
 responses is 1 bit time 
...
}
}
```

## Availability

| Since Version |
|---|
