# diagSendFunctional

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSendFunctional( diagRequest request)
```

## Description

Send a request to the functional group defined for the current target. The configuration of the functional transport protocol settings in the description configuration dialog must be present and consistent.

When used together with the built-in K-Line diagnostic channel, also the channel will be initialized to use functional addressing i.e. a functional startCommunication service will be put on the K-Line (Bit 6 & 7 of format byte set to 1) when the first request is sent. All subsequent requests sent with this function to the same target ECU will also carry the use functional addressing information.

In order to switch back to physical addressing, you have to call diagCloseChannel(ECU_Qualifier) and then DiagSetTarget(ECU_Qualifier) to prepare the re-opening of the channel upon the next request.

## Return Values

Error code

## Example

```c
on key 'f'
{
  diagRequest Serial_Number_Read req;
  long ret;
  if (0 != (ret=diagSetTarget("ECU1"))) write("diagSetTarget() failed with error code %ld!", ret);
  // Send request on functional channel
  if (0 != (ret=diagSendFunctional(req))) write("diagSendFunctional() failed with error code %ld!", ret);
}

on key 'p'
{
  diagRequest Serial_Number_Read req;
  long ret;
  // reset functional to physical addressing, if necessary
  if (0 != (ret=diagSetTarget("ECU1"))) write("diagSetTarget() failed with error code %ld!", ret);
  // Send request on physical channel
  if (0 != (ret=diagSendRequest(req))) write("diagSendRequest() failed with error code %ld!", ret);
}

on diagResponse Serial_Number_Read
{
  char ser_no[30];
  diagGetParameter(this, "Serial_Number", ser_no, elcount(ser_no));
  write("Response from serial no.: %s",ser_no);
}
```

## Availability

| Since Version |
|---|
