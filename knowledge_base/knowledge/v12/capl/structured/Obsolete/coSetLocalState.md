# coSetLocalState

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coSetLocalState( dword newState, dword errCode[] );
```

## Description

The function sets the communication state of the node. The node must previously have been started with coStartUp. The node layer controls the local communication state independently. Also a (configured) automatic transfer into the state Operational (Bit 2 in 1F80 not set) is caused by the node layer. Should it nevertheless be necessary to intervene directly in the local state machine, this can occur via this function.

After a successful call of this function, the new state is not yet assumed in each case since the processing of this command occurs asynchronously. The state change is signaled by the event function coOnNodeChangedState.

## Return Values

—

## Example

```c
dword errCode[1];

coSetLocalState( 5, errCode );
if (errCode[0] == 0) {
  write( "Local state change successfully commanded" );
}
```

## Availability

| Up to Version |
|---|
