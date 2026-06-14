# J1939ILControlWait

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILControlWait(); // form 1
```

## Description

Sending messages is suspended. Setting of signal is not possible.

Call J1939ILControlResume to activate sending again.

## Return Values

0 on success or error code

## Example

```c
on key 'w'
{
 J1939ILControlWait();
}
```

## Availability

| Since Version |
|---|
