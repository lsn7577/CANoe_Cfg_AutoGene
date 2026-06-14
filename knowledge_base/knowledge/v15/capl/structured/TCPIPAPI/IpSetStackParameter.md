# IpSetStackParameter

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpSetStackParameter(char parameterName[], long value); // form 1
long IpSetStackParameter(dword ifIndex, char parameterName[], long value); // from 2
```

## Description

With this function it is possible to modify the general behaviour of the TCP/IP Stack or the behaviour of an interface of the TCP/IP Stack. The name of the parameter is given as a path separated by dots.

The following values can be set by the function:

## Parameters

| Name | Description |
|---|---|
| ifIndex | The 1-based network interface index. |
| parameterName | A string representing the path to the parameter which should be set (e.g. net.inet.tcp.delayed_ack). |
| value | The value that should be set. |

## Example

```c
on start
{
  LONG result;
  LONG ifIndex;
  LONG value;

  // change maximum transmission unit of interface given in ifIndex
  ifIndex = 1;
  value = 1460;
  result = ipSetStackParameter(ifIndex, "canoe.interface.mtu", value);
  if(result != 0) {
    writeLineEx(1, 3, "Failed to set mtu of interface %d to %d byte. Result: %d", ifIndex, value, result);
  }
  else {
    writeLineEx(1, 0, "Set MTU of interface %d to %d byte.", ifIndex, value);
  }

  // change the ipv6 default scope to the interface given in ifIndex
  ifIndex = 1;
  result = ipSetStackParameter(ifIndex, "canoe.ipv6.default_scope", 1);
  if(result != 0) {
    writeLineEx(1, 3, "Failed to set ipv6 default scope to interface %d. Result: %d", ifIndex, result);
  }
  else {
    writeLineEx(1, 0, "Set ipv6 default scope to interface %d.", ifIndex);
  }

  // change the tcp delayed acknowlege behaviour
  value = 0;
  result = ipSetStackParameter("net.inet.tcp.delayed_ack", value);
  if(result != 0) {
    writeLineEx(1, 3, "Failed to change delayed acknowledge behaviour. Result: %d", result);
  }
  else {
    if( value == 0){
      writeLineEx(1, 0, "Successfully disabled TCP delayed acknowledge");
    }
    else{
      writeLineEx(1, 0, "Successfully enabled TCP delayed acknowledge");
    }
  }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 | 9.0 | 13.0 | — | — | 2.1 SP2 |
| Restricted To | IP | IP | IP | — | — | IP |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
