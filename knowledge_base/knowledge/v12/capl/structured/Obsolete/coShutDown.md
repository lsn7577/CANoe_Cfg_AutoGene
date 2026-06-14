# coShutDown

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coShutDown( dword deleteOD, dword errCode[] );
```

## Description

Stops the CANopen® communication of the node.

## Return Values

—

## Example

```c
dword errCode[1];

coShutDown( 1, errCode );
if (errCode[0] == 0) {
  write( "Shut down node with clearing object dictionary successfully" );
}
```

## Availability

| Up to Version |
|---|
