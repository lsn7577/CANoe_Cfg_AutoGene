# coLssIdentNonConfigSlave

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coLssIdentNonConfigSlave( dword errCode[] );
```

## Description

With this service, the LSS master commands all LSS slaves whose node-ID is not configured (0xFF) to identify themselves.

## Return Values

—

## Example

```c
dword errCode[1];

coLssIdentNonConfigSlave( errCode );
if (errCode[0] == 0) {
  write( "LSS identify non-configured slaves commanded" );
}
```

## Availability

| Up to Version |
|---|
