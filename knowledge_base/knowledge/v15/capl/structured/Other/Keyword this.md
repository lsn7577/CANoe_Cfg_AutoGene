# Keyword this

> Category: `Other` | Type: `notes`

## Description

Within an event procedure for receiving a CAN object or an environment variable, the data structure of the object is designated by the key word this.

For example, you could access the first data byte of message 100 which was just received by means of the following:

on message 100 {byte byte_0;byte_0 = this.byte(0);...}

Analogously, you could read the new value of the integer environment variable Switch which has just been changed by means of the following:

on envVar Switch {int val;val = getvalue(this);...}

on message 101{ float a = 0; a = this.Signal1.phys;}

on message 101{ float a = 0; a = $Signal1;}

Access to signal values using this | Selectors

| Note You should not change the value of this within an event procedure. However, to permit the use of this as a parameter, value changes made to this are not prohibited by the CAPL compiler. However, please note that these types of write accesses to this are only valid locally (i.e. within the event procedure). When compiling you will receive an appropriate warning. Thus, if you call the function output(this) after this has been changed in an on message event procedure, the unchanged original of this is passed, and not your change. |
|---|

| Note For a signal length of more than 32 bit the read out of signal values from a message with this.<signalName> is not yet supported. In this case the dollar notation must be used, see the example below. |
|---|

| Version 15© Vector Informatik GmbH |
|---|
