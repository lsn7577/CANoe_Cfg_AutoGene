# outputMostPktThis

> Category: `MOST` | Type: `function`

## Syntax

```c
outputMostPktThis();
```

## Description

Passes the packet on to the next node in the nodal sequence.

## Return Values

—

## Example

Packet filter in CAPL:

```c
OnMostPkt(long pktdatalen)
{
   // 
 filter destination address 0x100
   if(mostPktDestAdr() 
 == 0x100)
   {
      // 
 forward packet to the successor
      outputMostPktThis(); 
  
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.0 | 5.0 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 After measurement start | MOST25 MOST50 MOST150 After measurement start | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
