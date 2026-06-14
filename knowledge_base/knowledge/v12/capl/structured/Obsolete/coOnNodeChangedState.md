# coOnNodeChangedState

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coOnNodeChangedState( dword newState );
```

## Description

This function is called if the state of the node changes. This can be triggered by the functions coSetLocalState, coStartUp, coShutDown or via the network.

## Return Values

—

## Example

```c
void coOnNodeChangedState( dword newState ){
  write( "New state %d", newState );
}
```

## Availability

| Up to Version |
|---|
