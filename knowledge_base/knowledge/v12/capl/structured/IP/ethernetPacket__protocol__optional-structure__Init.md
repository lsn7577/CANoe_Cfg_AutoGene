# ethernetPacket::protocol::optional-structure::Init

> Category: `IP` | Type: `function`

## Syntax

```c
long ethernetPacket.<protocol>.<optional-structure>.Init();
```

## Description

Add a protocol option for a specific protocol to the Ethernet packet. The protocol must support options. Following options are available:

End of Option list

optionEOL

No Operation

optionNOP

Security

optionSecurity

Loose Source Routing

optionLooseSourceRoute

Internet Timestamp

optionTimeStamp

Record Route

optionRecordRoute

Stream ID

optionStreamID

Strict Source Routing

optionoptionStrictSourceRoute

Address Mask Reply

addrMaskReply

Addr Mask Request

addrMaskRequest

Alternate Host Address

alternateHostAddress

Datagram Conv Error

datagramConvError

Destination Unreachable

destinationUnreachable

Domain Name Reply

domainNameReply

Domain Name Request

domainNameRequest

Echo

echo

Echo Reply

echoReply

Information Reply

informationReply

Information Request

informationRequest

IPv 6 I Am Here

ipv6IAmHere

IPv 6 Where Are You

ipv6WhereAreYou

Mobile Host Redirect

mobileHostRedirect

Mobile Reg Reply

mobileRegReply

Mobile Reg Request

mobileRegRequest

Msg Utilized by Exp

msgUtilizedByExp

Parameter Problem

parameterProblem

Redirect

redirect

Router Advertisement

routerAdvertisement

routerSolicitation

securityFailures

skip

sourceQuench

timeExceeded

timestamp

timestampReply

traceroute

Hop-By-Hop Options

hopByHopOptions

Routing Header

routing

Fragment Header

fragment

Authentication Header

authentication

Encapsulating Security Payload

esp

Destination Options Header

destinationOptions

Echo Request

echoRequest

Home Agent Address Discovery Reply

homeAgentAddrDiscReply

Home Agent Address Discovery Request

homeAgentAddrDiscRequest

Mobile Prefix Advertisement

mobilePrefixAdvertisement

Mobile Prefix Solicitation

mobilePrefixSolicitation

Multicast Listener Done

multicastListenerDone

Multicast Listener Query

multicastListenerQuery

Multicast Listener Report

multicastListenerReport

Multicast Router Advertisement

multicastRouterAdvertisement

Multicast Router Solicitation

multicastRouterSolicitation

Multicast Router Termination

multicastRouterTermination

v2MulticastListernerReport

Inverse Advertisement

inverseAdvertisement

Inverse Solicitation

inverseSolicitation

Neighbor Advertisement

neighborAdvertisement

Neighbor Solicitation

neighborSolicitation

Router Solicitation

Membership Query

membershipQuery

Membership Report

membershipReport

Control

control

Acknowledge

ack

Error

error

File Data

fileData

Read Request

readRequest

Write Request

writeRequest

## Return Values

0 – Success

## Example

```c
on key '1'
{
  ethernetPacket pkt;
  pkt.ipv6.Init();// initialize a packet IPv6
  pkt.udp.Init(); // and UDP
  pkt.ipv6.fragment.Init();
  pkt.ipv6.fragment.offset = 100;
  pkt.ipv6.framgent.flag  = 1;
  pkt.ipv6.fragment.identification = 0x1234;
  pkt.CompletePacket();
  output( pkt );
}
```

## Availability

| Since Version |
|---|
