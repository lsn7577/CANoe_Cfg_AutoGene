# setStartdelay

> Category: `Other` | Type: `function`

## Syntax

```c
void setStartdelay(int delay)
```

## Description

Sets the value of the Start Delay for this network node. This function can only be called in the preStart event procedure. Afterwards the value of the Start Delay cannot be changed any more.

## Return Values

—

## Example

```c
...
on preStart
{
// Set Start Delay to 10 seconds
setStartdelay(10000);
}
```

## Availability

| Since Version |
|---|
