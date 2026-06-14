# CAPLfunctionCanResetStatistics

> Category: `CAN` | Type: `function`

## Syntax

```c
void canResetStatistics();
```

## Description

Resets CAN channel statistics.

There are two ways to call this function:

## Return Values

—

## Example

```c
on key 'r' 
{ 
   // reset statistics on CAN 1
   canResetStatistics(1);
}
```

## Availability

| Since Version |
|---|
