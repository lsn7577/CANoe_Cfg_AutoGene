# TestWaitForFrSymbol

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForFrSymbol (dword aTimeout);
```

## Description

Waits for the occurrence of a FlexRay symbol on the bus. Should the symbol not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Example

The following test program waits for the occurrence of different POC state events and symbols on one FlexRay bus.

```c
variables
{
  char bus1[20] = "FlexRay_1";
  char bus2[20] = "FlexRay_2";
  msTimer actionTimer;
  int  gAction = 0;
  const int gActionDelay = 52;   // [ms]
  const int gTimeout     = 300;  // [ms]
  const int gExtTimeout  = 2700; // [ms] to be waited additionally after cluster wake-up
  const int cPossibleWakeupDelay = 1500; // [ms] to be waited after possible cluster wake-up
  const int cWakeupDelay = 1500; // [ms] to be waited after cluster wake-up
  BYTE gSta1Id      = 5;  // slot ID for frame to send
  BYTE gSta1Flags   = 16; // event-triggered
  BYTE gSta1Dlc     = 4;  // bytes
  BYTE gSta1Chan    = 3;  // send on channel A+B
  BYTE gSta1Base    = 0;  // base cycle
  BYTE gSta1Rep     = 1;  // cycle repetition
}

testcase GoodCheckFlexRayWaitForSymbol_1 ()
{
  long result;
  FrSymbol frSymbolData;

  TestStepPass("Library: FrTFS_Wait_Symbol_POC.can", "Testcase: WaitForSymbol_Any");
  InitBusContext();
  _wakeupCluster(1);
  TestStep("Wait","waiting to assure running cluster...");
  TestWaitForTimeout(cPossibleWakeupDelay);
  TestStep("Prepare","Defining 'FlexRay symbol to be sent' action and triggering timer...");
  gAction = 1;
  actionTimer.set(gActionDelay);
  TestStep("Wait","Waiting for any FlexRay symbol...");
  TestStepPass("Call TFS function", "TestWaitForFrSymbol(timeout=%d)", gTimeout+1000);

  // The real test to be checked:
  result = TestWaitForFrSymbol(gTimeout+1000);
  if (result == 0)
  {
    TestStepFail("Timeout Occurred");
  }
  else if (result == -1)
  {
    TestStepFail("General Error");
  }
  else if (result == -2)
  {
    TestStepFail("Constraint Violation");
  }
  else
  {
    TestStepPass("Any FlexRay symbol successfully received!");
    TestStepPass("Call TFS function", "TestGetWaitFrSymbolData(frSymbolData)");
    // Test for data extraction:
    result = TestGetWaitFrSymbolData(frSymbolData);
    if (0 != result)
    {
      TestStepFail("Data extraction", "result = %d, Data access could not be executed.", result);
    }
    else
    {
      TestStepPass("Data extraction", "Data extraction works fine. Symbol=%d", frSymbolData.FR_Symbol);
    }
  }
}

testcase GoodCheckFlexRayWaitForPOC_1 ()
{
  long result;
  FrPOCState frPOCStateData;

  TestStepPass("Library: FrTFS_Wait_Symbol_POC.can", "Testcase: WaitForPOCState_Specific");
  InitBusContext();
  _wakeupCluster(1);
  TestStep("Wait","waiting to assure running cluster...");
  TestWaitForTimeout(cPossibleWakeupDelay);
  TestStep("Prepare","Defining 'Cluster to sleep mode' action and triggering timer...");
  gAction = 2;
  actionTimer.set(gActionDelay);
  TestStep("Wait","Waiting for POC state 'Halt (4)'...");
  TestStepPass("Call TFS function", "TestWaitForFrPOCState(4, timeout=%d)", gTimeout);

  // The real test to be checked:
  result = TestWaitForFrPOCState(4, gTimeout);
  if (result == 0)
  {
    TestStepFail("Timeout Occurred");
  }
  else if (result == -1)
  {
    TestStepFail("General Error");
  }
  else if (result == -2)
  {
    TestStepFail("Constraint Violation");
  }
  else
  {
    TestStepPass("FlexRay Interface is offline (asynchronous)!");
    TestStepPass("Call TFS function", "TestGetWaitFrPOCStateData(frPOCStateData)");
    result = TestGetWaitFrPOCStateData(frPOCStateData);
    if (0 != result)
    {
      TestStepFail("Data extraction", "result = %d, Data access could not be executed.", result);
    }
    else
    {
      TestStepPass("Data extraction", "Data extraction works fine. StateCode=%d", frPOCStateData.FR_POCState);
    }
  }
  TestStep("Wait","Waiting to assure sleeping cluster to be ready for wakeup...");
  TestWaitForTimeout(cWakeupDelay); // wait minimum time that cluster should sleep before wake-up
  TestStep("Prepare","Defining 'Wakeup Cluster' action and triggering timer...");
  gAction = 3;
  actionTimer.set(gActionDelay);
  TestStep("Wait","Waiting for POC state 'Normal Active (2)'...");
  TestStepPass("Call TFS function", "TestWaitForFrPOCState(2, timeout=%d)", gTimeout+gExtTimeout);

  // The real test to be checked:
  result = TestWaitForFrPOCState(2, gTimeout+gExtTimeout);
  if (result == 0)
  {
    TestStepFail("Timeout Occurred");
  }
  else if (result == -1)
  {
    TestStepFail("General Error");
  }
  else if (result == -2)
  {
    TestStepFail("Constraint Violation");
  }
   else
  {
    TestStepPass("FlexRay Interface is online (synced)!");
    TestStepPass("Call TFS function", "TestGetWaitFrPOCStateData(frPOCStateData)");
    // Test for data extraction:
    result = TestGetWaitFrPOCStateData(frPOCStateData);
    if (0 != result)
    {
      TestStepFail("Data extraction", "result = %d, Data access could not be executed.", result);
    }
    else
    {
      TestStepPass("Data extraction", "Data extraction works fine. StateCode=%d", frPOCStateData.FR_POCState);
    }
  }
}

testcase GoodCheckFlexRayWaitForWUS_1 ()
{
  long result;
  FrPOCState frPOCStateData;

  TestStepPass("Library: FrTFS_Wait_Symbol_POC.can", "Testcase: WaitForWakeupState_Any");
  InitBusContext();
  _wakeupCluster(1);
  TestStep("Wait","waiting to assure running cluster...");
  TestWaitForTimeout(cPossibleWakeupDelay);
  TestStep("Prepare","Defining 'Cluster to sleep mode' action and triggering timer...");
  gAction = 2;
  actionTimer.set(gActionDelay);

  TestStep("Wait","Waiting for POC state 'Halt (4)'...");
  result = TestWaitForFrPOCState(4, gTimeout);
  if (result == 0)
  {
    TestStepFail("Timeout Occurred");
  }
  else if (result == -1)
  {
    TestStepFail("General Error");
  }
  else if (result == -2)
  {
    TestStepFail("Constraint Violation");
  }
  else
  {
    TestStepPass("FlexRay Interface is offline (asynchronous)!");
  }

  TestStep("Wait","Waiting to assure sleeping cluster to be ready for wakeup...");
  TestWaitForTimeout(cWakeupDelay); // wait minimum time that cluster should sleep before wake-up
  TestStep("Prepare","Defining 'Wakeup Cluster' action and triggering timer...");
  gAction = 3;
  actionTimer.set(gActionDelay);

  TestStep("Wait","Waiting for any Wakeup state...");
  TestStepPass("Call TFS function", "TestWaitForFrPOCState(-1, 0, timeout=%d)", gTimeout+gExtTimeout);

  // The real test to be checked:
  result = TestWaitForFrPOCState(-1, 0, gTimeout+gExtTimeout);
  if (result == 0)
  {
    TestStepFail("Timeout Occurred");
  }
  else if (result == -1)
  {
    TestStepFail("General Error");
  }
  else if (result == -2)
  {
    TestStepFail("Constraint Violation");
  }
  else
  {
    TestStepPass("Any Wakeup state received!");
    TestStepPass("Call TFS function", "TestGetWaitFrPOCStateData(frPOCStateData)");
    // Test for data extraction:
    result = TestGetWaitFrPOCStateData(frPOCStateData);
    if (0 != result)
    {
      TestStepFail("Data extraction", "result = %d, Data access could not be executed.", result);
    }
    else
    {
      TestStepPass("Data extraction", "Data extraction works fine. WUSCode=%d", frPOCStateData.FR_Info2);
    }
  }
}

on timer actionTimer
{
  if (gAction == 1)
  {
    FrSendSymbol(0,0,1);
    TestStepPass("FlexRay MTS Symbol sent!");
  }
  else if (gAction == 2)
  {
    _cmdClusterToSleep(1);
    TestStepPass("Cmd 'Cluster to sleep mode' sent!");
  }
  else if (gAction == 3)
  {
    _wakeupCluster(1);
   TestStepPass("Wakeup pattern sent!");
  }
  gAction = 0;
}

void _cmdClusterToSleep (int channel)
{
  // ATTENTION: The command is sent via a FlexRay frame. The cluster's nodes must implement this feature!

  BYTE gSta1Msg[254]; // message buffer
  gSta1Msg[0] = 0x95;
  gSta1Msg[1] = 0x95;
  gSta1Msg[2] = 0x0b;
  gSta1Msg[3] = 0xb8;
  FRSendFrame(gSta1Id /*frameId*/, gSta1Chan /*channelMask*/, gSta1Dlc /*len*/, gSta1Base /*cycleStart*/, gSta1Rep /*cycleRepetition*/, gSta1Flags /*flags*/, gSta1Msg /*dataBytes*/, channel);
}

void _wakeupCluster (int channel)
{
  int wuChMask = 1;    // send wake-up on channel A
  int wuCount  = 4;    // send symbol 4 times (range 2-63)
  int wuTxIdle = 180;  // idle time of symbol in bit (range 0-255)
  int wuTxLow  = 60;   // low time of symbol in bit (range 0-63)
  char cfg[200];

  ResetFlexRayCCEx(channel,wuChMask,wuCount,wuTxIdle,wuTxLow,cfg);
}

void InitBusContext ()
{
  dword context;
  TestStep("Prepare","Setting bus context..");
  context = GetBusNameContext(bus2);
  if (context > 0)
    setBusContext(context);
  else
  {
    TestStepFail("Bus context cannot be set");
  }
}
```

## Availability

| Since Version |
|---|
