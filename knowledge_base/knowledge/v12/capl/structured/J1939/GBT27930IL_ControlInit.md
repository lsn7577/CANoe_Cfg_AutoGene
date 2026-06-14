# GBT27930IL_ControlInit

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_ControlInit(); // form 1
```

## Description

This function can only be used in on preStart, to suppress the auto-start function of the IL.

## Return Values

0 on success or error code

## Example

```c
on preStart
{
 GBT27930IL_ControlInit();
}
```

## Availability

| Since Version |
|---|
