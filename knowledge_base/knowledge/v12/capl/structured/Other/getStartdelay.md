# getStartdelay

> Category: `Other` | Type: `function`

## Syntax

```c
int getStartdelay()
```

## Description

Determines the value of the start delay configured for this network node in the Simulation Setup.

## Return Values

Start delay in ms. If no start delay was set the function returns the value zero.

## Example

```c
int val;
...
// Assign to val the value of the start delay
val = getStartdelay();
...
```

## Availability

| Since Version |
|---|
