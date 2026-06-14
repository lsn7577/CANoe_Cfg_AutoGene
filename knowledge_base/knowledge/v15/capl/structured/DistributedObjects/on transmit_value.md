# on transmit_value

> Category: `DistributedObjects` | Type: `event`

## Description

This handler is called whenever a provided data, event, or field member transmits a value via the CAPL binding.

If the member does not use the CAPL binding, the handler is ignored.

If there are multiple handlers for the same member, the measurement will be aborted. Inside the handler the this expression refers to the value of the member (i.e. it is of type valueHandle <Member type>).

## Example

```c
// transmit an event via CAN messages

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
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | ✔ | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | ✔ | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | ✔ | ✔ | N/A |
