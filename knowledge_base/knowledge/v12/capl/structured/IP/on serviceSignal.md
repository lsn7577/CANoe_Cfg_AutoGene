# on serviceSignal

> Category: `IP` | Type: `event`

## Syntax

```c
on serviceSignal <signal>
```

## Description

This function is called when the signal value is changed and the associated SOME/IP message has been received. Within the callback function you have direct access to the signal value via keyword this:

this

Access to the physical value of the Service Signal

FLOAT

this.raw

Access to the raw value of the Service Signal

this.raw64

QWORD

## Example

The parameter Param1_CommonDataType is contained in Event1 of service Service1 (Major Version 1, Instance ID 2). The service interface is defined in package PACKAGE1::PACKAGE2 of database DemoDatabase.

```c
// the following function is called if the Service Signal value was changed
on serviceSignal DemoDatabase::PACKAGE1::PACKAGE2::Service1::1::2::Event1::Param1_CommonDataType
{
  int   rwaValue;
  float physValue;

  rwaValue  = this.raw;
  physValue = this;

  write("Service Signal changed: Service Signal 'Param1_CommonDataType' received (physical value: %f, raw value: %d)", physValue, rwaValue);
}
```

## Availability

| Since Version |
|---|
