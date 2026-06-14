# coLssInqNodeId

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coLssInqNodeId( dword errCode[] );
```

## Description

This service causes the determination of the node-ID of a LSS slave. It is available in configuration mode only and there may only be one LSS slave in this mode.

## Return Values

—

## Example

```c
dword errCode[1];

coLssInqNodeId( errCode );
if (errCode[0] == 0) {
  write( "LSS inquire node-ID commanded" );
}
```

## Availability

| Up to Version |
|---|
