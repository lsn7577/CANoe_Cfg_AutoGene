# IpGetStackParameter

> Category: `TCPIPAPI` | Type: `function`

## Syntax

```c
long IpGetStackParameter(char parameterName[], long value);
```

## Description

With this function it is possible to read the value of a TCP/IP Stack parameter. The name of the parameter is given as a path separated by dots.

The following values can be read by the function:

## Return Values

0: The function completed successfully.

## Example

```c
on start
{
  LONG result;
  LONG ifIndex;
  LONG value;

  // get the maximum transmission unit of the interface given in ifIndex
  ifIndex = 1;
  result = ipGetStackParameter(ifIndex, "canoe.interface.mtu", value);
  if(result != 0) {
    writeLineEx(1, 3, "Failed to get mtu of interface %d. Result: %d", ifIndex, result);
  }
  else {
    writeLineEx(1, 0, "MTU of interface %d is %d byte.", ifIndex, value);
  }

  // get the ipv6 default scope
  result = ipGetStackParameter("canoe.ipv6.default_scope", value);
  if(result != 0) {
    writeLineEx(1, 3, "Failed to get ipv6 default scope. Result: %d", result);
  }
  else {
    writeLineEx(1, 0, "IPv6 default scope is set to interface %d.", value);
  }

  // get the tcp delayed acknowlege behaviour
  result = ipGetStackParameter("net.inet.tcp.delayed_ack", value);
  if(result != 0) {
    writeLineEx(1, 3, "Failed to get delayed acknowledge behaviour. Result: %d", result);
  }
  else {
    if( value == 0){
      writeLineEx(1, 0, "TCP delayed acknowledge is disabled");
    }
    else{
      writeLineEx(1, 0, "TCP delayed acknowledge is enabled");
    }
  }
}
```

## Availability

| Since Version |
|---|
