# GNSSGetCurLat

> Category: `J1939` | Type: `function`

## Syntax

```c
double GNSSGetCurLat();
```

## Description

The function returns the current latitude at which the receiver is located. If a value of 0.0 is returned, the GNSSGetLastError function must be used to check whether the value is valid (see error codes).

## Return Values

current latitude (in degrees)

## Example

```c
double lat;
lat = GNSSGetCurLat();

if (lat == 0 && GNSSGetLastError() != 0 ) {
  write(“Error: Invalid current latitude”);
}
```

## Availability

| Since Version |
|---|
