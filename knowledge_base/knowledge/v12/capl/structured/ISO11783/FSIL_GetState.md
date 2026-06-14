# FSIL_GetState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_GetState(); // form 1
```

## Description

Returns the current state of the FS IL.

## Return Values

0: Initialized

## Example

```c
on key 's'
{
  long state;
  state = FSIL_GetState();
}
```

## Availability

| Since Version |
|---|
