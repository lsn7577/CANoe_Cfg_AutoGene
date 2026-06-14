# coGetLocalState

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword coGetLocalState( dword errCode[] );
```

## Description

This function returns the current communication state of the node. It is not necessary to determine the state permanently since a state change is signaled by the event function coOnNodeChangedState.

## Return Values

Current communication state of the node
4 - stopped5 - operational6 - reset node7 - reset communication127 - pre-operational
The states reset node and reset communication are transient states. This means they are not static and are only run through. The node then automatically goes to state pre-operational.

## Example

```c
dword errCode[1];

if (coGetLocalState( errCode ) == 5) {
  /* change process data */
}
```

## Availability

| Up to Version |
|---|
