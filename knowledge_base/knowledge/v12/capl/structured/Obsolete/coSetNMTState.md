# coSetNMTState

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coSetNMTState( dword nodeId, dword newState,dword errCode[] );
```

## Description

Sets the state of a node on the network. The node for which this function is called must previously have been started with coStartUp(). Furthermore, the node must be configured as NMT master (Bit 0 in 1F80 set) and the object 1F82 must exist in the object dictionary.

## Return Values

—

## Example

```c
dword errCode[1];

coSetNMTState( 0, 5, errCode );
if (errCode[0] == 0) {
  write( "NMT state change to Operational for all nodes commanded" );
}
```

## Availability

| Up to Version |
|---|
