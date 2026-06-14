# SetServiceSignalData

> Category: `IP` | Type: `function`

## Syntax

```c
long SetServiceSignalData(serviceSignal qualifier, byte buffer [], dword bufferLength); // form 1
```

## Description

Sets the data of a Service Signal.

## Return Values

0: no error, function successful.

## Example

The example shows access to parameter StringValue, which is contained in Event1 of service Service1 (Major Version 1, Instance ID 2). The service interface is defined in package PACKAGE1::PACKAGE2 of database DemoDatabase.

The service qualifier is specified without a leading $ sign.

```c
on key 's'
{
  byte buffer[1] = {0x12};

SetServiceSignalData(DemoDatabase::PACKAGE1::PACKAGE2::Service1::1::2::Event1::StringValue, buffer, elcount(buffer));
}
```

## Availability

| Since Version |
|---|
