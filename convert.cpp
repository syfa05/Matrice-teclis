
  
  Aspose::Cells::Startup();
  
  Workbook wkb(u"input.prn"));
  wkb.Save(u"Output.xlsx");

  Aspose::Cells::Cleanup();
	