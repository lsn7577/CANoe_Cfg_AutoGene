# J1939CalcChecksum

> Category: `J1939` | Type: `function`

## Syntax

```c
dword J1939CalcChecksum( pg * parameterGroup );
```

## Description

This function calculates the checksum of a parameter group.

PGNs, for which the checksum should be calculated, as well as the computational method are defined in the J1939/71 specification.

This function can be used for sending a message (to calculate the checksum) and for receiving a message (to validate the transmitted checksum).

## Return Values

The calculated checksum, if a computational method is defined (see J1939/71 specification), else "-1".
Range of valid values:

## Example

Calculation for sending

Validation for receiving

```c
on start
{
  pg TSC1 tsc1;
  setTimer(Timer1, 1000);
  tsc1.MessageCounter = 0x0;
  nextSeqCounterForTSC1 = 0x1;
}

void SendMyMessage()
{
  pg TSC1 tsc1;

  tsc1.SA = 0;
  tsc1.DA = 33;

  // set values for signals that represent sequence counter and checksum
  if(tsc1.MessageCounter == 0x7)
    tsc1.MessageCounter = 0;
  else if(tsc1.MessageCounter < 0x7)
    tsc1.MessageCounter += 1;

  tsc1.MessageChecksum = J1939CalcChecksum(tsc1);

  output( tsc1 );
}
variables
{
  long lastSeqCounterForTSC1 = 0; //start value
}

on pg TSC1
{
  int expectedChecksum, expectedCounter;

  //Check message counter
  if(this.MessageCounter == 0xF) //MessageCounter isn't used at all
    expectedCounter = 0xF;
  else
    expectedCounter = nextSeqCounterForTSC1;

  if (this.MessageCounter != nextSeqCounterForTSC1)
  {
    // Error handling
    write("TSC1: wrong message counter (expected: %d, observed: %d)",
    expectedCounter, this.MessageCounter);
  }

  //calculate next value for the message counter
  if(this.MessageCounter == 0x7)
    nextSeqCounterForTSC1 = 0;
  else if(this.MessageCounter < 0x7)
    nextSeqCounterForTSC1 = this.MessageCounter + 1;

  //Check message checksum
  expectedChecksum = J1939CalcChecksum(this);
  if (this.MessageChecksum != expectedChecksum)
  {
    // Error handling
    write("TSC1: wrong message checksum (expected: %d, observed: %d)",
    expectedChecksum, this.MessageChecksum);
  }
}
```

## Availability

| Since Version |
|---|
