# Iso11783IL_OPChangePriority

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783IL_OPChangePriority( dword maskID, dword priority ); // form 1
```

## Description

The function changes the priority of an alarm mask. A Change Priority command is sent to the Virtual Terminal.

## Return Values

0: Function has been executed successfully

## Example

```c
Iso11783IL_OPChangePriority( 1200, 2 );
```

## Availability

| Since Version |
|---|
