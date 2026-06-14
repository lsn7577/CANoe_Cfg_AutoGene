# getGPSTimeString

> Category: `Other` | Type: `function`

## Syntax

```c
void getGPSTimeString(char timeBuffer[], dword timestamp);
```

## Description

Copies a printed representation of the GPS time stamp represented as UTC date and time into the supplied character buffer. The format of the string is ddd mmm dd hh:mm:ss jjjj (e.g. "Fri Aug 21 15:22:24 1998").

## Return Values

—

## Example

```c
variables
{
  char UTC_time_and_date_buffer[30]; // needs min. 26 chars
  dword UnixTimestamp;
}

on start
{
  getGPSTimeString(UTC_time_and_date_buffer, UnixTimestamp);
}
```

## Availability

| Since Version |
|---|
