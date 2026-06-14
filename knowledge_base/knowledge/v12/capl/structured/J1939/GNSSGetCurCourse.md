# GNSSGetCurCourse

> Category: `J1939` | Type: `function`

## Syntax

```c
double GNSSGetCurCourse( void )
```

## Description

This function returns the current course in degrees along which the GNSS receiver is moving.

If a value of 0.0 is returned, the GNSSGetLastError function must be used to check whether the value is valid (see error codes).

## Return Values

current course in degrees

## Example

```c
double course;
course = GNSSGetCurCourse();
write(“Course = %lf degree”, course);
```

## Availability

| Since Version |
|---|
