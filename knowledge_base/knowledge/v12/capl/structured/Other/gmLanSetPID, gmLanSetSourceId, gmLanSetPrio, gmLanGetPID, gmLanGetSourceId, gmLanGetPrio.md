# gmLanSetPID, gmLanSetSourceId, gmLanSetPrio, gmLanGetPID, gmLanGetSourceId, gmLanGetPrio

> Category: `Other` | Type: `function`

## Syntax

```c
gmLanSetPID(gmLanMessage msg, long v);
```

## Description

gmLanSetPID sets the parameter ID of the message.

gmLanSetSourceId sets the source address of the message.

gmLanSetPrio sets the priority of the message.

gmLanGetPID gets the parameter ID of the message.

gmLanGetSourceId gets the source address of the message.

gmLanGetPrio gets the priority of the message.

## Return Values

gmLanSetPID, gmLanSetSourceId, gmLanSetPrio: —

## Example

A GMLAN message is modified and sent with output(msg).The parameter ID is set with selector gm_pid.

Priority and source address are copied from Battery_Voltage message to the new message msg:

```c
gmLanMessage * msg1 ={SA =0x44, PRIO=  0x7,  gm_pid=0x11};
gmLanSetSourceId(msg1,0x55);
gmLanSetPID(msg1,0x11);
gmLanSetPrio(msg1,0x5); 

output(msg1);

write("pid: 0x%x, source: 0x%x, prio:  x%x",gmLanGetPID(msg1),gmLanGetSourceId(msg1),gmLanGetPrio(msg1));
on gmlanmessage  Battery_Voltage 
{
  gmlanmessage Battery_Voltage msg;
  msg = this;  // SA and PRIO are not copied
  gmLanSetSourceId(msg, gmLanGetSourceId(this));
  // Copy  source address from Battery_Voltage to msg
  gmLanSetPrio(msg,  gmLanGetPrio(this));
  // Copy priority from Battery_Voltage to msg
  ...
}
```

## Availability

| Since Version |
|---|
