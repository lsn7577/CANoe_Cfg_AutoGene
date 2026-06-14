# linSetInterByteSpace

> Category: `LIN` | Type: `function`

## Syntax

```c
dword linSetInterByteSpace (long frameID, long index, dword sixteenthBits)
```

## Description

With this function it is possible to set an inter-byte space for a specified frame and a specified byte filed. The byte field may belong to the frame header as well as to the frame response.

Inter-byte space is the period between the end of the stop bit of the preceding byte and the start bit of the following byte.

By default the inter-byte space is 0.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 's'
{
if ( linSetInterByteSpace(0x33, 9, 32) != 0)
{
// from now on for frame ID=0x33 the inter-byte space 
 between last data byte field
// and Checksum byte is 2 bit times
...
}
}
```

## Availability

| Since Version |
|---|
