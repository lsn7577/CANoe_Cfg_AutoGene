# Binding::ValueReceived

> Category: `DistributedObjects` | Type: `method`

## Syntax

```c
long Binding::ValueReceived(distObjDataRef * member, double value);
long Binding::ValueReceived(distObjDataRef * member, long value);
long Binding::ValueReceived(distObjDataRef * member, dword value);
long Binding::ValueReceived(distObjDataRef * member, int64 value);
long Binding::ValueReceived(distObjDataRef * member, qword value);
long Binding::ValueReceived(distObjDataRef * member, char value[]);
long Binding::ValueReceived(distObjDataRef * member, dataTypeHandle value);
long Binding::ValueReceived(distObjEventRef * member, double value);
long Binding::ValueReceived(distObjEventRef * member, long value);
long Binding::ValueReceived(distObjEventRef * member, dword value);
long Binding::ValueReceived(distObjEventRef * member, int64 value);
long Binding::ValueReceived(distObjEventRef * member, qword value);
long Binding::ValueReceived(distObjEventRef * member, char value[]);
long Binding::ValueReceived(distObjEventRef * member, dataTypeHandle value);
long Binding::ValueReceived(distObjFieldRef * member, double value);
long Binding::ValueReceived(distObjFieldRef * member, long value);
long Binding::ValueReceived(distObjFieldRef * member, dword value);
long Binding::ValueReceived(distObjFieldRef * member, int64 value);
long Binding::ValueReceived(distObjFieldRef * member, qword value);
long Binding::ValueReceived(distObjFieldRef * member, char value[]);
long Binding::ValueReceived(distObjFieldRef * member, dataTypeHandle value);
```

## Description

Sets a value of a consumed data, event, or field member value that uses the CAPL binding.

The called overload must correspond to the member value type. Otherwise an error code is returned.

## Parameters

| Name | Description |
|---|---|
| member | Member which receives a value via the CAPL binding. |
| value | Value to be received. |

## Example

```c
// Transmit an event via CAN messages.

// example.vcdl
version 1.3;
namespace SomeNamespace {
  interface Example {
    [Binding="CAPL", CommunicationPattern=SendReceive]
    consumed event int32 SomeEvent;
  }
  object Consumer : Example {}
  object Provider : reverse<Example> {}
}

// provider.can
on key 'a' {
  $Provider.SomeEvent++;
}

// provider_binding.can
on transmit_value Provider.SomeEvent {
  message SomeEvent_Value msg;
  msg.value = $this;
  output(msg);
}

// consumer.can
on value_update Consumer.SomeEvent {
  write("received %d", $this);
}

// consumer_binding.can
on message SomeEvent_Value {
  Binding::ValueReceived(Consumer.SomeEvent, (long)this.value);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 14 | 14 | 15 | 15 | 5.0 SP3 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
