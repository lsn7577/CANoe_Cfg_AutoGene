# Example: TestReportAdd* Functions

> Category: `Test` | Type: `notes`

## Description

Color usage

statements keywords comments test functions

MainTest()

{

...

// add information to SUT information table

TestReportAddSUTInfo("Serial No.", "A012345BC");

TestReportAddSUTInfo("Manufactured", "2003-10-02");

// add information to test engineer information table

TestReportAddEngineerInfo("Test Engineer", "S. Grey");

TestReportAddEngineerInfo("Stuff No.", "12345");

// add information to test setup information table

TestReportAddSetupInfo("Tester", "TH12");

// add html line to report, e.g. a link to the homepage

TestReportAddExtendedInfo("html", "<A HREF=\"http://www.vector.com\">Homepage</A>");

}

testcase Configure_Powermanagement ()

// add info block to test case in report

TestReportAddMiscInfoBlock("Used Test Parameters");

TestReportAddMiscInfo("Max. voltage", "19.5 V");

TestReportAddMiscInfo("Max. current", "560 mA");

// add image to report, scale down to reasonable size

TestReportAddImage("Oscilloscope Snapshot", "osc_01.png", "400px", "");
