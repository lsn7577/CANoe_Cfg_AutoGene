# J1939ILOnChangedState

> Category: `J1939` | Type: `function`

## Syntax

```c
void J1939ILOnChangedState( long state )
```

## Description

This callback function is called from the J1939 IL if it has changed its state.

## Return Values

—

## Example

```c
void J1939ILOnChangedState( LONG state )
{
  switch(state) {
    case 1: // Claiming
      break;
    case 2: // Active
      break;
    case 3: // Stopped
      break;
    case 4: // Suspended
      break;
  }
}
```

## Availability

| Since Version |
|---|
