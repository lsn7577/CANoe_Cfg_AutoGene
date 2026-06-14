# GNSSGetCurAlt

> Category: `J1939` | Type: `function`

## Syntax

```c
double GNSSGetCurAlt();
```

## Description

The function returns the current altitude at which the receiver is located. If a value of 0.0 is returned, the GNSSGetLastError function must be used to check whether the value is valid (see error codes).

The unit of the altitude depends on the system of measurement units selected with the GNSSSetUnits function.

## Return Values

current altitude (in m or ft)

## Example

```c
double alt;
alt = GNSSGetCurAlt();

if (alt == 0 && GNSSGetLastError() != 0 ) {
  write(“Error: Invalid current altitude”);
}
```

## Availability

| Since Version |
|---|
