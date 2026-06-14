# TestWaitForEthernetPacket

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForEthernetPacket(qword sMAC, qword dMAC, word vlanID, word etherType, dword flags, dword aTimeout); // form 1
```

## Description

Waits for the occurrence of the first Ethernet packet matching the conditions passed as arguments. Should the message not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no message is specified the wait condition is resolved on any message.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

## Return Values

-2: Resume due to constraint violation

## Example

```c
void MainTest ()
{
  long result;
  dword timeout;
  byte ipv6AddrAny[16]; // Any's IPv6 address bytes.
  byte ipv6AddrAlice[16]; // Alice's IPv6 address bytes.

  // form 1 - waits for the occurrence of any Ethernet packet
  result = TestWaitForEthernetPacket(0, 0, 0, 0, 0, timeout);

  // form 1 - waits for the occurrence of any AVTP packet tagged with VLAN ID 9
  result = TestWaitForEthernetPacket(0, 0, 9, 0x22F0, 0, timeout);

  // form 2 - waits for the occurrence of any IPv4 packet with a 0.0.0.0 source IPv4 address
  result = TestWaitForEthernetPacket(IpGetAddressAsNumber("0.0.0.0"), 0, 0, 0, 0, 0x0020, timeout);

  // form 3 - waits for the occurrence of any IPv6 packet with the destination IPv6 address of 
  // Alice -> 2001:DB8:85A3:8D3:1319:8A2E:370:7344
  IpGetAddressAsArray("::", ipv6AddrAny);
  IpGetAddressAsArray("2001:DB8:85A3:8D3:1319:8A2E:370:7344", ipv6AddrAlice);
  result = TestWaitForEthernetPacket(ipv6AddrAny, ipv6AddrAlice, 0, 0, 0, 0, timeout);

  // form 4 - waits for the occurrence of any UDP datagramm transported over IPv4 containing MQTT information
  result = TestWaitForEthernetPacket(0, 0, 0, 0, 0, 0, 17, 0, 1883, 0, timeout);

  // form 5 - waits for the occurrence of any TCP segment transported over IPv6 containing
  // FTP information coming from MAC address 12:34:56:78:9A:BC and Alice's IPv6
  result = TestWaitForEthernetPacket(0x0000123456789ABCLL, 0, 0, 0, ipv6AddrAlice, 
  ipv6AddrAny, 6, 0, 20, 0, timeout);

  // form 6 - waits for the occurrence of any Ethernet, IPv4 or IPv6 packet exchanged between
  // the two database nodes ADAS and CAMF.
  TestWaitForEthernetPacket(ADAS, CAMF, 0, 0, 0, 0, timeout);
}
```

## Availability

| Since Version |
|---|
