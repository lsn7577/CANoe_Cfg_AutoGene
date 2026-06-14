# coLssStoreConfig

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coLssStoreConfig( dword errCode[] );
```

## Description

The configured parameters are written into non-volatile memory with this service. Only one LSS slave may be in configuration mode.

## Return Values

—

## Example

```c
dword errCode[1];

coLssStoreConfig( errCode );
if (errCode[0] == 0) {
  write( "LSS store configuration commanded" );
}
```

## Availability

| Up to Version |
|---|
