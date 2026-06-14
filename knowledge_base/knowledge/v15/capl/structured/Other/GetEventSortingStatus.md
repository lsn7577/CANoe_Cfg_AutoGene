# GetEventSortingStatus

> Category: `Other` | Type: `function`

## Syntax

```c
int GetEventSortingStatus(message msg);
int GetEventSortingStatus(pg msg);
int GetEventSortingStatus(gmLanMessage msg);
int GetEventSortingStatus(linFrame msg);
int GetEventSortingStatus(mostMessage msg);
int GetEventSortingStatus(mostAmsMessage msg);
int GetEventSortingStatus(mostRawMessage msg);
int GetEventSortingStatus(j1587Param msg);
int GetEventSortingStatus(linBaudrateEvent event);
int GetEventSortingStatus(linCsError event);
int GetEventSortingStatus(linDlcinfo event);
int GetEventSortingStatus(linReceiveError event);
int GetEventSortingStatus(linSchedulerModeChange event);
int GetEventSortingStatus(linSlaveTimeout event);
int GetEventSortingStatus(linSleepModeEvent event);
int GetEventSortingStatus(linSyncError event);
int GetEventSortingStatus(linTransmError event);
int GetEventSortingStatus(linWakeupFrame event);
int GetEventSortingStatus(beanError event);
int GetEventSortingStatus(mostLightLockError event);
int GetEventSortingStatus(FRSlot event);
int GetEventSortingStatus(FRFrame msg);
int GetEventSortingStatus(FrStartCycle event);
```

## Description

Determines the Event Sorting state.

With active Event Sorting the return value indicates if the given event in the Simulation Setup of CANoe was processed in correct time sequence.

## Parameters

| Name | Description |
|---|---|
| Message event variable of type | "message", "pg", "gmLanMessage", "linFrame", "mostMessage", "mostAmsMessage", "mostRawMessage", "j1587Param", "linBaudrateEvent", "linCsError", "linDlcinfo", "linReceiveError", "linSchedulerModeChange", "linSlaveTimeout", "linSleepModeEvent", "linSyncError", "linTransmError", "linWakeupFrame", "beanError", "mostLightLockError", "FRSlot", "FRFrame" or "FrStartCycle". |

## Example

```c
on message *
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on linSlaveTimeout
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on linTransmError
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on linCsError
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on linReceiveError
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on linSyncError
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on pg *
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on gmLanMessage *
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}  
}
on linFrame *
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on mostMessage *
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on mostRawMessage
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on mostAMSMessage *
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on J1587Param *
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event", (double)this.msgOrigTime/100000 );
}
}
on linBaudrateEvent
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on linDlcInfo
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on linSchedulerModeChange
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on linSleepModeEvent
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on linWakeupFrame
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on mostLightLockError
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on FRSlot *
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on FRFrame *
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
on FRStartCycle *
{
if ( GetEventSortingStatus(this)==2 )  {
Write("Unsorted Event at time %.6f", (double)this.time/100000 );
}
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.0 | 6.0 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | ✔ | N/A |
