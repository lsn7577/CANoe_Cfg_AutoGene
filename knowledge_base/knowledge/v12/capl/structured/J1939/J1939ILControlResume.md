# J1939ILControlResume

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILControlResume(); // form 1
```

## Description

After suspending the J1939 IL with J1939ILControlWait, this function restarts the IL. The J1939 IL starts sending cyclic messages again.

## Return Values

0 on success or error code

## Example

```c
on key 'r'
{
 J1939ILControlResume();
}
```

## Availability

| Since Version |
|---|
