# GetServiceSignalString

> Category: `IP` | Type: `function`

## Syntax

```c
long GetServiceSignalString(serviceSignalString qualifier, char buffer [], dword bufferLength); // form 1
```

## Description

Reads the string value of a Service Signal.

## Return Values

>=0: Length of the string that has been fetched from the Service Signal.

## Example

The example shows access to parameter StringValue, which is contained in Event1 of service Service1 (Major Version 1, Instance ID 2). The service interface is defined in package PACKAGE1::PACKAGE2 of database DemoDatabase.

The service qualifier is specified without a leading $ sign.

```c
on key 'r'
{
  char buffer[255];
  GetServiceSignalString(DemoDatabase::PACKAGE1::PACKAGE2::Service1::1::2::Event1::StringValue, buffer, elcount(buffer));

  write("Actual value of Service Signal StringValue: %s",buffer);
}
```

## Availability

| Since Version |
|---|
