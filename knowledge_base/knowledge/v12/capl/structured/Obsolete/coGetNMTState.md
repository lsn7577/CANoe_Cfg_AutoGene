# coGetNMTState

> Category: `Obsolete` | Type: `function`

## Syntax

```c
dword coGetNMTState( dword nodeId, dword errCode[] );
```

## Description

Returns the state of a node on the network. The node for which this function is called must previously have been started with coStartUp. Furthermore, the node must be configured as NMT master (Bit 0 in 1F80 set) and the object 1F82 must exist in the object dictionary.

The NMT state of a node can only be determined if it is monitored.

## Return Values

Current communication state of the node
0 - unknown or failed4 - stopped5 - operational127 - pre-operational

## Example

```c
dword errCode[1];
dword nmtState;

nmtState = coGetNMTState( 10, errCode );
if (errCode[0] == 0){
  write( "NMT state successfully requested" );
}
if (nmtState == 5)
{
  write( "Node 10 is operational" );
}
```

## Availability

| Up to Version |
|---|
