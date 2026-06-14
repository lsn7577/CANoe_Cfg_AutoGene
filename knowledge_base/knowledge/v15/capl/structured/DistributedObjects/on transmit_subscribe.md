# on transmit_subscribe

> Category: `DistributedObjects` | Type: `event`

## Description

This handler is called whenever a consumed data, event, or field member transmits a subscribe via the CAPL binding.

If the member does not use the CAPL binding, the handler is ignored.

If there are multiple handlers for the same member, the measurement will be aborted.

## Example

```c
// Transmit a subscription request via CAN.
//
// This example requires a CAN message "SomeData_Request" with a
// signal "Request" and a CAN message "SomeData_Answer" with a
// signal "Answer".

// example.vcdl
version 1.3;
namespace SomeNamespace {
  interface Example {
    [Binding="CAPL", AutoSubscribe=false]
    consumed data int32 SomeData;
  }
  object Consumer : Example {}
  object Provider : reverse<Example> {}
}

// consumer.can
variables {
  using namespace _SystemDataTypes::SDStates;
}
on key 'a' {
  // toggle subscription state
  if ($Consumer.SomeData.SubscriptionState == DOMemberSubscription::Unsubscribed)
    Consumer.SomeData.Subscribe();
  else
    Consumer.SomeData.Unsubscribe();
}

// consumer_binding.can
variables {
  using namespace _SystemDataTypes::SDStates;
}
on transmit_subscribe Consumer.SomeData {
  message SomeData_Request msg;
  Binding::SubscriptionStateReceived(Consumer.SomeData, DOMemberSubscription::Requested);
  msg.Request = DOMemberSubscription::Requested;
  output(msg);
}
on transmit_unsubscribe Consumer.SomeData {
  message SomeData_Request msg;
  msg.Request = DOMemberSubscription::Unsubscribed;
  output(msg);
}
on message SomeData_Answer {
  Binding::SubscriptionStateReceived(Consumer.SomeData, this.Answer);
}

// provider.can
on key 'b' {
  $Provider.SomeData++;
}

// provider_binding.can
variables {
  using namespace _SystemDataTypes::SDStates;
  enum DOMemberSubscription consumerState;
}
on message SomeData_Request {
  message SomeData_Answer msg;
  consumerState = this.Request == DOMemberSubscription::Requested ?
  DOMemberSubscription::Subscribed :
  DOMemberSubscription::Unsubscribed;
  msg.Answer = consumerState;
  output(msg);
}
on transmit_value Provider.SomeData {
  // value not transmitted via CAN, just set it directly
  if (consumerState == DOMemberSubscription::Subscribed)
  Binding::ValueReceived(Consumer.SomeData, $this);
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
