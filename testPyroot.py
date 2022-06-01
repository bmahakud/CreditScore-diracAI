import ROOT


hAttendance = ROOT.TH1F("hAttendance", "hAttendance", 50, 0, 1)
hAttendance.GetXaxis().SetTitle("Attendance in fraction of days");
hAttendance.GetYaxis().SetTitle("Frequency");



hAlertness = ROOT.TH1F("hAlertness", "hAlertness", 50, 0, 1)
hAlertness.GetXaxis().SetTitle("Alertness in fraction of days");
hAlertness.GetYaxis().SetTitle("Frequency");




hHomework = ROOT.TH1F("hHomework", "hHomework", 50, 0, 1)
hHomework.GetXaxis().SetTitle("Home work in fraction of days");
hHomework.GetYaxis().SetTitle("Frequency");


rng1 = ROOT.TRandom3(1)
rng2 = ROOT.TRandom3(2)
rng3 = ROOT.TRandom3(3)


hPerformance = ROOT.TH1F("hPerformance", "Performance", 50, 0, 1)


h2DAlertAttendance = ROOT.TH2F("h2DAlertAttendance","h2DAlertAttendance",50,0,1,50,0,1);


h2DAlertAttendance.GetXaxis().SetTitle("Alertness");
h2DAlertAttendance.GetYaxis().SetTitle("Attendance");


ftrain = open("TrainData.txt", "w")
ftest = open("TestData.txt","w")

#f.write("Now the file has more content!")




for i in range(3000):
    value1 = rng1.Gaus(50,2);
    value2 = rng2.Gaus(45,2);
    value3 = rng2.Gaus(40,4);
    nvalue1 = round(value1/60, 2);
    nvalue2 = round(value2/60, 2);
    nvalue3 = round(value3/60, 2);
    hAttendance.Fill(nvalue1);
    hAlertness.Fill(nvalue2);
    hHomework.Fill(nvalue3);
    Pvalue = round((nvalue1*0.4) + (nvalue2*0.2) +(0.4*nvalue3),3)
    h2DAlertAttendance.Fill(nvalue1,nvalue2);

    hPerformance.Fill(Pvalue);
    print (nvalue1," ", nvalue2," ", nvalue3," ", Pvalue)
    #print (("%.2f" % round(nvalue1, 2)), ("%.2f" % round(nvalue3, 2)),("%.2f" % round(nvalue3, 2)), ("%.2f" % round(Pvalue, 2)))
    if i < 2000:
         ftrain.write(str(nvalue1)+" "+str(nvalue2)+" "+str(nvalue3)+" "+str(Pvalue)+"\n");
    if i >2000:
         ftest.write(str(nvalue1)+" "+str(nvalue2)+" "+str(nvalue3)+" "+str(Pvalue)+"\n");
 









c1=ROOT.TCanvas("c1","c1")
c1.cd();
hAttendance.Draw()
c1.SaveAs("Attendance.png");


c2=ROOT.TCanvas("c2","c2")
c2.cd();
hAlertness.Draw()
c2.SaveAs("Alertness.png");

c3=ROOT.TCanvas("c3","c3")
c3.cd();
hHomework.Draw()
c3.SaveAs("Homework.png");



c4=ROOT.TCanvas("c4","c4")
c4.cd();
hPerformance.Draw();


c5 = ROOT.TCanvas("c5","c5");
c5.cd();
h2DAlertAttendance.Draw('colz');
c5.SaveAs("AlertnessAttendance.png");




