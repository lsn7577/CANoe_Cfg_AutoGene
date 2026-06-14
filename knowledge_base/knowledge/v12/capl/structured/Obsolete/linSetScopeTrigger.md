# linSetScopeTrigger

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long linSetScopeTrigger (long ID, long Position)
```

## Description

With these functions it is possible to define trigger conditions for an oscilloscope. If the trigger conditions are satisfied, the LIN hardware will send an impulse on the sync cable.

The first function defines a single trigger condition for a valid frame or an error in a response.

The second function defines a set of trigger conditions.

If this function is called from on preStart part of the CAPL program, then this function will have no effect.

## Return Values

On success, a value unequal to zero, otherwise zero.

## Example

```c
on key 'a'
{
long lresp;
long position=0;

// The fourth parameter is a Byte Array (8 Bytes).
// -> 64 Bits for the setting of 64 Ids.

byte idmask[8] = {0,0,0,0,0,0,0,0};
byte identifier = 0x30;

// Byte Position: 6         // Bit Position: 0 
idmask[identifier / 8] |= 1 << (identifier % 8);

lresp = linSetScopeTrigger (0x30, position);
lresp = linSetScopTrigger (1, 1, 1, idmaks);
}
```

## Availability

| Up to Version |
|---|
