# J1939ILControlStop

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939ILControlStop(); // form 1
```

## Description

Deactivates the IL and stops sending cyclic messages.

A Cannot Claim Address message is sent, if the NMT is activated and the message is not suppressed with the parameter option set to 1.

## Return Values

0 on success or error code

## Example

```c
on key 's'
{
 J1939ILControlStop(1);
}
```

## Availability

| Since Version |
|---|
