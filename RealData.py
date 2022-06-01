import ROOT


hAttendance = ROOT.TH1F("hAttendance", "hAttendance", 20, 0, 30)
hAttendance.GetXaxis().SetTitle("Number of students in class");
hAttendance.GetYaxis().SetTitle("Frequency");
#hAttendance.SetBinErrorOption(ROOT.TH1::kPoisson))


data = [10,13,5,13,13,13,11,13,13,6,12,13,4,11,9,13,13,11,13,13,12,13,10,13,13,4,13,13]

data2 = [28,28,24,25,24,24,24,24,26,25,24,25,25]


for num in data2:
    hAttendance.Fill(num)


c1 = ROOT.TCanvas("c1","c1");
c1.cd();
hAttendance.Draw("E");
c1.SaveAs("Attendance.png");




