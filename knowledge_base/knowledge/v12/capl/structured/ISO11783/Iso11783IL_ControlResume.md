# Iso11783IL_ControlResume

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_ControlResume();
```

## Description

After suspending the ISO11783 IL with Iso11783IL_ControlWait, this function restarts the IL. The ISO11783 IL starts sending cyclic messages again.

## Return Values

0 on success or error code

## Example

```c
on key 'r'
{
 Iso11783IL_ControlResume();
}
```

## Availability

| Since Version |
|---|
