# ethResetStatistics

> Category: `IP` | Type: `function`

## Syntax

```c
void ethResetStatistics( long channel );
```

## Description

Resets Ethernet channel statistics. The Ethernet channel statistics are provided by the Eth<channel> object.

## Return Values

Value range: 1..32

## Example

```c
on key 'i'
{
  ethResetStatistics( 1 ); // Reset statistics of Eth 1
}
```

## Availability

| Since Version |
|---|
