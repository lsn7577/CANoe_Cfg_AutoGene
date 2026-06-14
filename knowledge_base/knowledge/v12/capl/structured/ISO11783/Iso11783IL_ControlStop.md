# Iso11783IL_ControlStop

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_ControlStop();
```

## Description

Deactivates the IL and stops sending cyclic messages. A Cannot Claim Address message is sent, if the NMT is activated and the message is not suppressed with the parameter option set to 1.

## Return Values

0 on success or error code

## Example

```c
on key 's'
{
 Iso11783IL_ControlStop(1);
}
```

## Availability

| Since Version |
|---|
