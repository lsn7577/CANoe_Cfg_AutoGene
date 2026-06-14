# GetEventSortingStatus

> Category: `Other` | Type: `function`

## Syntax

```c
int GetEventSortingStatus(message msg);
```

## Description

Determines the Event Sorting state.

With active Event Sorting the return value indicates if the given event in the Simulation Setup of CANoe was processed in correct time sequence.

## Return Values

0: Invalid state
The Event Sorting is inactive or it concerns a program internal event that will never be sorted (e.g. environment variable).

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

| Since Version |
|---|
