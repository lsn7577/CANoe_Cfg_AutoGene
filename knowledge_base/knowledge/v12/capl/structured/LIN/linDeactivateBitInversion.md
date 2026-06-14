# linDeactivateBitInversion

> Category: `LIN` | Type: `function`

## Syntax

```c
long LINDeactivateBitInversion()
```

## Description

With this function it is possible to cancel a previously activated bits inversion for LIN header or response. This function is useful when after calling linInvertHeaderBit() no header occurred yet on the bus or when after calling linInvertRespBit() no frame occurred yet.

## Return Values

On success a value unequal to zero, otherwise zero.

## Example

Deactivate previous bit inversion

```c
on key 'd'
{
   if (0==linDeactivateBitInversion())
   {
      write("CAPL: Bit inversion deactivation failure!");
   }
}
```

## Availability

| Since Version |
|---|
