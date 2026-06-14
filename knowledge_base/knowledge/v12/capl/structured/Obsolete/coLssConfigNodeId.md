# coLssConfigNodeId

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coLssConfigNodeId( dword nodeId, dword errCode[] );
```

## Description

With this service, the LSS master configures the node-ID of a LSS slave. Only one LSS slave may be in configuration mode.

## Return Values

—

## Example

```c
dword errCode[1];

coLssConfigNodeId( 1, errCode );
if (errCode[0] == 0) {
  write( "LSS configure nodeId commanded" );
}
```

## Availability

| Up to Version |
|---|
