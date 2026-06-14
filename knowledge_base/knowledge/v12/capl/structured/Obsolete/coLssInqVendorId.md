# coLssInqVendorId

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coLssInqVendorId( dword errCode[] );
```

## Description

This service causes the determination of the vendor-ID of a LSS slave. It is available in configuration mode only and there may only be one LSS slave in this mode.

## Return Values

—

## Example

```c
dword errCode[1];

coLssInqVendorId( errCode );
if (errCode[0] == 0) {
  write( "LSS inquire Vendor-ID commanded" );
}
```

## Availability

| Up to Version |
|---|
