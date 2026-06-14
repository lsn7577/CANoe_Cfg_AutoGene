# on ethernetPhyState

> Category: `IP` | Type: `event`

## Description

The event procedure is called on the change of the state of an Ethernet PHY or if a relevant PHY activity has been triggered.

To access the control information you would use selectors.

The key word this is available within an on ethernetPhyState procedure, to access the information of the PHY state and event type.

## Example

```c
on ethernetPhyState *
{
  ethernetport myPort;
  myPort = this.hwPort;
  switch(this.phyState)
  {
    case 1:
      write("Ethernet PHY on %s is in normal state", this.name);
      break;
    case 2:
      write("Ethernet PHY on %s is in sleep state", this.portname);
      break;
    case 3:
      write("Ethernet PHY %s of segment %s is in powerOff state",
      myPort.name, myPort.segmentName);
      break;
    case 4:
      write("Ethernet PHY on %s is in sleep_request state", myPort.name);
      break;
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 15 | 15 | 15 | — | — | 6 |
| Restricted To | Ethernet | Ethernet | Ethernet | — | — | Ethernet |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |

## Selectors

| Selector | Description | Type | Access Limitation |
|---|---|---|---|
| hwPort | Port associated with the PHY. | ethernetPort | network-based access only |
| time_ns | Time stamp of the PHY event | int64 | read only |
| phystate | 1: Normal state 2: Sleep state 3: PowerOff state 4: SleepRequest state | int32 | read only |
| eventtype | 1: Sleep received 2: Sleep sent 3: Sleep abort 4: Sleep ACK received 5: Sleep forwarded 8: Wakeup received 9: Wakeup sent 10: Wakeup forwarded 17: Power Off 18: Power On 25: PHY activated | int32 | read only |
| network-based | ../../../CANoeCANalyzer/Ethernet/EthernetPortBasedNetworkAccess.htm |  |  |
