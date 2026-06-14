# on serviceSignal_update

> Category: `IP` | Type: `event`

## Description

This function is called when the associated SOME/IP message has been received. It is immaterial whether or not the signal value was changed. Within the callback function you have direct access to the signal value via keyword this:

## Example

Note

The parameter Param1_CommonDataType is contained in Event1 of service Service1 (Major Version 1, Instance ID 2). The service interface is defined in package PACKAGE1::PACKAGE2 of database DemoDatabase.

```c
// the following function is called if the Service Signal value was updated
on serviceSignal_update DemoDatabase::PACKAGE1::PACKAGE2::Service1::1::2::Event1::Param1_CommonDataType
{
  int   rwaValue;
  float physValue;

  rwaValue  = this.raw;
  physValue = this;

  write("Service Signal update: Service Signal 'Param1_CommonDataType' received (physical value: %f, raw value: %d)", physValue, rwaValue);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 | 13.0 | — | — | 2.0 SP2 |
| Restricted To | — | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
