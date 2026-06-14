# J1939ILControlInit

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILControlInit(); // form 1
```

## Description

This function can only be used in on preStart, to suppress the auto-start function of the IL.

## Return Values

0 on success or error code

## Example

```c
on preStart
{
 J1939ILControlInit();
}
```

## Availability

| Since Version |
|---|
