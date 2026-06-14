# TCIL_GetState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long TCIL_GetState(); // form 1
```

## Description

Returns the current state of the TC IL.

## Return Values

0: Initialized

## Example

```c
on key 's'
{
  long state;
  state = TCIL_GetState();
}
```

## Availability

| Since Version |
|---|
