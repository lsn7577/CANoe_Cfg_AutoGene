# Iso11783OPChangePriority

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long Iso11783OPChangePriority( dword ecuHandle, dword maskID, dword priority );
```

## Description

The function changes the priority of an alarm mask. A Change Priority command is sent to the Virtual Terminal.

## Return Values

0 or error code

## Example

```c
Iso11783OPChangePriority( handle, 1200, 2 );
```

## Availability

| Since Version |
|---|
