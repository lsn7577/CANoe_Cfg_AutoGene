# KLine_SetInitType

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_SetInitType(long initType)
```

## Description

Configures the used initialization pattern.

Restriction: It is only possible to change the init type between the pre-configured init type an no init pattern. It is not possible to change between fast init and 5 baud init or vice versa.

## Return Values

On success 0, otherwise a value less than 0.

## Example

Example shows a test case that makes sure that an ECU does not respond to a request after a S3 timeout.

```c
DiagRequest TesterPresent req;
long timeout_ms;
int status;
DiagSetTarget(“DUT”);

// Connect Channel
DiagConnectChannel()
status = TestWaitForDiagChannelConnected(2000);
   if (1 == status)
   {
      TestStepPass("Connected to target ECU");
   }
   else
   {
      TestStepFail("Error connecting to target ECU.”);
   }

req.SendRequest();
   if (1 != TestWaitForDiagRequestSent(req, 1000))
   {
      TestStepFail(“Request was not sent.”);
   }
   if (1 != TestWaitForDiagResponse(req, 1000))
   {
      TestStepFail(“No response received.”);
   }

// StopCommunication command shall NOT be  send after closing the channel.
KLine_SuppressAutomaticStopCommunication(1);
DiagCloseChannel();
   if (1== TestWaitForDiagChannelClosed(1000))
   {
      TestStepPass( "Channel closed successfully.");
   }
   else
   {
      TestStepFail( "Channel could not be closed.");
   }
   KLine_SetInitType(3);   // No Init

// Wait for a S3 timout
timeout_ms = 6000;
TestWaitForTimeout(timeout_ms);

// Send again a tester present request
req.SendRequest();
TestWaitForDiagRequestSent(req, 1000);
   if  (1 == TestWaitForDiagResponse(req, 1000))
   {
      TestStepFail(“Request answered in spite of  a S3 timeout ”);
   }
   else
   {
      TestStepPass(“Request not answered due to S3 timeout.”);
   }

DiagCloseChannel();
   if (1== TestWaitForDiagChannelClosed(1000))
   {
      TestStepPass( "Channel closed successfully.");
   }
   else
   {
   TestStepFail( "Channel could not be closed.");
   }

// Reset Settings
KLine_SetInitType(2); // Fast Init
KLine_SuppressAutomaticStopCommunication(0);
```

## Availability

| Since Version |
|---|
