# frResetStatistics

> Category: `FlexRay` | Type: `function`

## Syntax

```c
void frResetStatistics();
```

## Description

Resets FlexRay cluster statistics. Both A and B channels are concerned.

There are two ways to call this function:

## Return Values

—

## Example

```c
on key 'r' 
{ 
   // reset statistics for A and B channels in cluster 1
   frResetStatistics(1);
}
```

## Availability

| Since Version |
|---|
