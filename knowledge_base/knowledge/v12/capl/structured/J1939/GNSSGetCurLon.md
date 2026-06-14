# GNSSGetCurLon

> Category: `J1939` | Type: `function`

## Syntax

```c
double GNSSGetCurLon();
```

## Description

The function returns the current longitude at which the receiver is located. If a value of 0.0 is returned, the GNSSGetLastError function must be used to check whether the value is valid (see error codes).

## Return Values

current longitude (in degrees)

## Example

```c
double lon;
lon = GNSSGetCurLon();

if (lon == 0 && GNSSGetLastError() != 0 ) {
  write(“Error: Invalid current longitude”);
}
```

## Availability

| Since Version |
|---|
