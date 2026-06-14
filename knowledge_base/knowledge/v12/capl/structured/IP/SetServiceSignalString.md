# SetServiceSignalString

> Category: `IP` | Type: `function`

## Syntax

```c
long SetServiceSignalString(serviceSignalString qualifier, char buffer []); // form 1
```

## Description

Sets the string value of a Service Signal. The function automatically appends the respective byte order mark (BOM) depending on the data type (UTF8 or UTF16).

## Return Values

0: no error, function successful.

## Example

The example shows access to parameter StringValue, which is contained in Event1 of service Service1 (Major Version 1, Instance ID 2). The service interface is defined in package PACKAGE1::PACKAGE2 of database DemoDatabase.

The service qualifier is specified without a leading $ sign.

```c
on key 's'
{
SetServiceSignalString(DemoDatabase::PACKAGE1::PACKAGE2::Service1::1::2::Event1::StringValue,"Hello World");
}
```

## Availability

| Since Version |
|---|
