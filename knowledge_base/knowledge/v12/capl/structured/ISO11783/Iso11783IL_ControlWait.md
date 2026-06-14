# Iso11783IL_ControlWait

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_ControlWait();
```

## Description

Sending messages is suspended. Setting of signal is not possible.

Call Iso11783IL_ControlResume to activate sending again.

## Return Values

0 on success or error code

## Example

```c
on key 'w'
{
 Iso11783IL_ControlWait();
}
```

## Availability

| Since Version |
|---|
