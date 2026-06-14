# J1939TestCaseComment

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestCaseComment( char comment[], pg commentPG )
```

## Description

Writes the data of a parameter group variable as comment to the test protocol.

## Example

```c
pg EEC1 aPG;
J1939TestCaseComment( "EEC1:", aPG );
```

## Availability

| Since Version |
|---|
