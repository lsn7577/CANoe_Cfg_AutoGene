# coLssInqProdCode

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coLssInqProdCode( dword errCode[] );
```

## Description

This service causes the determination of the product code of a LSS slave. It is available in configuration mode only and there may only be one LSS slave in this mode.

## Return Values

—

## Example

```c
dword errCode[1];

coLssInqProdCode( errCode );
if (errCode[0] == 0) {
  write( "LSS inquire Product-Code commanded" );
}
```

## Availability

| Up to Version |
|---|
