# GNSSOnWpBeforeLastReached

> Category: `J1939` | Type: `function`

## Syntax

```c
void GNSSOnWpBeforeLastReached();
```

## Description

This function is called when the next-to-last waypoint of the waypoint list has been reached. This makes it possible to insert an additional waypoint before the GNSS receiver comes to a stop.

## Return Values

—

## Example

```c
// Implementation of a loop
void GNSSOnWpBeforeLastReached()
{
  GNSSAddWpRel( 20.0, 0.0, 0.0 );
}
```

## Availability

| Since Version |
|---|
