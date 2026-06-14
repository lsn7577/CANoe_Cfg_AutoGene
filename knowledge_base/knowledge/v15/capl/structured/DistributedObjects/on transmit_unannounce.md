# on transmit_unannounce

> Category: `DistributedObjects` | Type: `event`

## Description

This handler is called whenever a provided data, event, or field member transmits an unannounce via the CAPL binding.

If the member does not use the CAPL binding, the handler is ignored. If there are multiple handlers for the same member, the measurement will be aborted.

## Example

```c
// example.vcdl
version 1.3;
namespace SomeNamespace {
  interface Example {
    [Binding="CAPL", HasAnnounceAPI=true]
    provided data int32 SomeData;
  }
  object Consumer : reverse<Example> {}
  object Provider : Example {}
}

// consumer_binding.can
variables {
  using namespace _SystemDataTypes::SDStates;
}
on transmit_subscribe Consumer.SomeData {
  Binding::SubscriptionStateReceived(Consumer.SomeData, DOMemberSubscription::Subscribed);
}

// provider.can
variables {
  using namespace _SystemDataTypes::SDStates;
}
on key 'a' {
  // toggle announcement
  if ($Provider.SomeData.AnnouncementState == DOMemberAnnouncement::Unannounced)
    Provider.SomeData.Announce();
  else
    Provider.SomeData.Unannounce();
}
on key 'b' {
  // increment value
  $Provider.SomeData++;
}

// provider_binding.can
variables {
  using namespace _SystemDataTypes::SDStates;
  enum DOMemberAnnouncement registry[char[]];
}
on transmit_announce Provider.SomeData {
  registry[Provider.SomeData.Path] = DOMemberAnnouncement::Announced;
  Binding::AnnouncementStateReceived(Provider.SomeData, DOMemberAnnouncement::Announced);
}
on transmit_unannounce Provider.SomeData {
  registry[Provider.SomeData.Path] = DOMemberAnnouncement::Unannounced;
  Binding::AnnouncementStateReceived(Provider.SomeData, DOMemberAnnouncement::Unannounced);
}
on transmit_value Provider.SomeData {
  if (registry[Provider.SomeData.Path] == DOMemberAnnouncement::Announced)
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
