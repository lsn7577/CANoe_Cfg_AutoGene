# Example: writeClear, writeCreate, writeDestroy, writeEx, writeLineEx

> Category: `Other` | Type: `notes`

## Description

variables{long mNewPage; // Sink identifier}on start{//Create a new page at the Write WindowmNewPage= writeCreate("New Page");//Configure the page so that its content is loggedwriteConfigure(mNewPage, 20, 1, "c:\\temp\\writelog.TXT");//Clear content of CAPL pagewriteclear(1);//Show the description of the programwriteLineEx(mNewPage,2,"This program shows the keyboard sequence in a new created Page ");writeLineEx(mNewPage,4,"\nKeyboard sequence: ");}on key *{//show the current key at the "New Page"char currentKey;currentKey = this;writeEx(mNewPage,4,"%c ",currentKey);}on stopMeasurement{//destroy the new created PagewriteDestroy(mNewPage);}
