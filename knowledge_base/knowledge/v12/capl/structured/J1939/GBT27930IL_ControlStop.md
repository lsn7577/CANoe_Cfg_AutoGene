# GBT27930IL_ControlStop

> Category: `J1939` | Type: `function`

## Syntax

```c
long GBT27930IL_ControlStop(); // form 1
```

## Description

Deactivates the IL and stops sending cyclic messages.

## Return Values

0 on success or error code

## Example

```c
on key 's'
{
 GBT27930IL_ControlStop(1);
}
```

## Availability

| Since Version |
|---|
