# VTIL_OnChangedState

> Category: `ISO11783` | Type: `function`

## Syntax

```c
void VTIL_OnChangedState( long state );
```

## Description

This callback function is called from the VT IL if it has changed its state.

## Return Values

—

## Example

```c
void VTIL_OnChangedState( long state )
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
