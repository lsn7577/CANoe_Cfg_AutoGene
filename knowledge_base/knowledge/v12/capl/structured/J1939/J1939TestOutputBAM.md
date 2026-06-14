# J1939TestOutputBAM

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestOutputBAM( pg txMsg, dword seqNum, dword seqCount, dword delay, [dword options], [dword optionArg] )
```

## Description

With this function the transmission of a message with the BAM transport protocol is influenced. It can created errors during transmission, i.e. violate time distances or wrong sequence numbers.

## Example

```c
pg EC1 txMsg = { DLC=38 };

// send BAM and first Data message
J1939TestOutputBAM( txMsg, 0, 2, 50 );

// send Data message, Seq. 2
J1939TestOutputBAM( txMsg, 2, 1, 350 );

// the DUT should detect, that the time between Seq 2 and Seq 3 is more than 200ms 
// send Data message, Seq. 3 to 6
J1939TestOutputBAM( txMsg, 3, 4, 50 );
```

## Availability

| Since Version |
|---|
