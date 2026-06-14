# C2xSecCertificateGetHandle

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xSecCertificateGetHandle( char name[] );
```

## Description

Gets a certificate handle from a certificate listed in the Car2x Certificate Manager

## Return Values

Handle of the certificate or 0 on failure

## Example

```c
// assumes a certificate with name "MyCert" was added to the configuration in the Car2x Certificate Manager dialog

long certificateHandle;
certificateHandle = C2xSecCertificateGetHandle( "MyCert" );
```

## Availability

| Since Version |
|---|
