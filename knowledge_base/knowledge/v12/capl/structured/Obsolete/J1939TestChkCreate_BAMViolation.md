# J1939TestChkCreate_BAMViolation

> Category: `Obsolete` | Type: `function`

## Syntax

```c
long J1939TestChkCreate_BAMViolation(dword min, dword max, dword options);
```

## Description

Observes the BAM transport protocol. It is possible to observer all BAM transmissions or only the transmission of a specific send node.

## Example

```c
long bamCheck;
bamCheck = J1939TestChkCreate_BAMViolation( EMS, 50, 200, 0x00 );

J1939TestChkControl_Start(bamCheck);
TestAddConstraint(bamCheck);
```

## Availability

| Up to Version |
|---|
