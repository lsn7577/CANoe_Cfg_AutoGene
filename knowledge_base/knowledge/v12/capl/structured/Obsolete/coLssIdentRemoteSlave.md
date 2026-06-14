# coLssIdentRemoteSlave

> Category: `Obsolete` | Type: `function`

## Syntax

```c
void coLssIdentRemoteSlave( dword vendorId, dword productCode, dword revisionNoLow, dword revisionNoHigh, dword serialNoLow, dword serialNoHigh, dword errCode[] );
```

## Description

With this service the LSS master commands all LSS slaves whose LSS address matches the transmitted LSS address parameters to identify themselves.

## Return Values

—

## Example

```c
dword errCode[1];

/* get values from environment variables */
dword vendorId = getValue(envVendorId);
dword productCode = getValue(envProductCode);
dword revNoLow = getValue(envRevNoLow);
dword revNoHigh = getValue(envRevNoHigh);
dword serialNoLow = getValue(envSerialNoLow);
dword serialNoHigh = getValue(envSerialNoHigh);

coLssIdentRemoteSlave( vendorId, productCode, revNoLow, revNoHigh, serialNoLow, serialNoHigh );
```

## Availability

| Up to Version |
|---|
