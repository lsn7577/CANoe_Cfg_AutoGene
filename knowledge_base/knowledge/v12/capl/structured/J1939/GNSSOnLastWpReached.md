# GNSSOnLastWpReached

> Category: `J1939` | Type: `function`

## Syntax

```c
void GNSSOnLastWpReached();
```

## Description

This function is called when the last waypoint of the waypoint list has been reached. The GNSS receiver waits at this point until a new waypoint is inserted into the waypoint list.

## Return Values

—

## Example

```c
void GNSSOnLastWpReached()
{
  write( "Last waypoint is reached" );
}
```

## Availability

| Since Version |
|---|
