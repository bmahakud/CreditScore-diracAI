import ROOT

hAttendance = ROOT.TH1F("Attendance", "Attendance", 100, 0, 100)
hAttendance.GetXaxis().SetTitle("Attendance in %age");
hAttendance.GetYaxis().SetTitle("Frequency");
hAttendance.SetFillColor(2);


hAlertness = ROOT.TH1F("Alertness", "Alertness", 100, 0, 100);
hAlertness.GetXaxis().SetTitle("Alertness in %age");
hAlertness.GetYaxis().SetTitle("Frequency");
hAlertness.SetFillColor(3);


hHomework = ROOT.TH1F("Homework", "Homework", 100, 0, 100)
hHomework.GetXaxis().SetTitle("Home work in %age");
hHomework.GetYaxis().SetTitle("Frequency");
hHomework.SetFillColor(4);


hUnderstanding = ROOT.TH1F("Understanding", "Understanding", 10, 0, 10)
hUnderstanding.GetXaxis().SetTitle("Rating provided by the students");
hUnderstanding.GetYaxis().SetTitle("Number of students");
hUnderstanding.SetFillColor(5);

hPreviousPerformance = ROOT.TH1F("PreviousPerformance", "PreviousPerformance", 100, 0, 100)
hPreviousPerformance.GetXaxis().SetTitle("Previous Exam performance in %age marks");
hPreviousPerformance.GetYaxis().SetTitle("Number of students");
hPreviousPerformance.SetFillColor(6);






hAttendanceN = ROOT.TH1F("AttendanceN", "AttendanceN", 200, 0, 1)
hAttendanceN.GetXaxis().SetTitle("Attendance in fraction of days");
hAttendanceN.GetYaxis().SetTitle("Frequency");
hAttendanceN.SetFillColor(2);

hAlertnessN = ROOT.TH1F("AlertnessN", "AlertnessN", 200, 0, 1);
hAlertnessN.GetXaxis().SetTitle("Alertness in fraction of days");
hAlertnessN.GetYaxis().SetTitle("Frequency");
hAlertnessN.SetFillColor(3);


hHomeworkN = ROOT.TH1F("HomeworkN", "HomeworkN", 200, 0, 1)
hHomeworkN.GetXaxis().SetTitle("Home work in fraction of days");
hHomeworkN.GetYaxis().SetTitle("Frequency");
hHomeworkN.SetFillColor(4);

hUnderstandingN = ROOT.TH1F("UnderstandingN", "UnderstandingN", 10, 0, 1)
hUnderstandingN.GetXaxis().SetTitle("Rating provided by the students");
hUnderstandingN.GetYaxis().SetTitle("Number of students");
hUnderstandingN.SetFillColor(5);

hPreviousPerformanceN = ROOT.TH1F("PreviousPerformanceN", "PreviousPerformanceN", 200, 0, 1)
hPreviousPerformanceN.GetXaxis().SetTitle("Previous Exam performance");
hPreviousPerformanceN.GetYaxis().SetTitle("Number of students");
hPreviousPerformanceN.SetFillColor(6);










hPerformance = ROOT.TH1F("hPerformance", "Performance", 50, 0, 1)
hPerformance.SetFillColor(46);
hPerformance.GetXaxis().SetTitle("Exam score normalized");
hPerformance.GetYaxis().SetTitle("Number of students");




h2DAlertAttendance = ROOT.TH2F("h2DAlertAttendance","h2DAlertAttendance",50,0,1,50,0,1);
h2DAlertAttendance.GetXaxis().SetTitle("Alertness");
h2DAlertAttendance.GetYaxis().SetTitle("Attendance");


rng1 = ROOT.TRandom3(1)
rng2 = ROOT.TRandom3(2)
rng3 = ROOT.TRandom3(3)
rng4 = ROOT.TRandom3(4)
rng5 = ROOT.TRandom3(23);



ftrain = open("TrainData.txt", "w")
ftest = open("TestData.txt","w")

#f.write("Now the file has more content!")




for i in range(3000):
    attendance = rng1.Gaus(70,2);
    alertness = rng2.Gaus(60,2);
    homework = rng3.Gaus(40,4);
    understanding = rng4.Gaus(6,2);
    prePerformance = rng5.Gaus(70,3);
    hAttendance.Fill(attendance);
    hAlertness.Fill(alertness);
    hHomework.Fill(homework);
    hUnderstanding.Fill(understanding);
    hPreviousPerformance.Fill(prePerformance);

    hAttendanceN.Fill(attendance/100);
    hAlertnessN.Fill(alertness/100);
    hHomeworkN.Fill(homework/100);
    hUnderstandingN.Fill(understanding/10);
    hPreviousPerformanceN.Fill(prePerformance/100);

    AttendanceN=round(attendance/100,3);  
    AlertnessN=round(alertness/100,3);
    HomeworkN=round(homework/100,3);
    UnderstandingN=round(understanding/10,3);
    PreviousPerformanceN=round(prePerformance/100,3);

    print (AttendanceN," ", AlertnessN," ", HomeworkN," ", UnderstandingN," ",PreviousPerformanceN)


    Theta_zero=0.2;
    Theta_attendance=0.3;
    Theta_alertness=0.05;
    Theta_homework=0.4;
    Theta_understanding=0.1;
    Theta_prevperformance=0.15;
    meanPerformance=Theta_zero+(Theta_attendance*AttendanceN)+(Theta_alertness*AlertnessN)+(Theta_homework*HomeworkN)+(Theta_understanding*UnderstandingN)+(Theta_prevperformance*PreviousPerformanceN)
    performance=round(rng4.Gaus(meanPerformance, 0.05),3);
    hPerformance.Fill(performance);
    if i < 2000:
         ftrain.write(str(AttendanceN)+" "+str(AlertnessN)+" "+str(HomeworkN)+" "+
                 str(UnderstandingN)+" "+str(PreviousPerformanceN)+" "+str(performance)+"\n");
   
    if i > 2000:
         ftest.write(str(AttendanceN)+" "+str(AlertnessN)+" "+str(HomeworkN)+" "+
                 str(UnderstandingN)+" "+str(PreviousPerformanceN)+" "+str(performance)+"\n");


 








'''
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
hUnderstanding.Draw();
c4.SaveAs("Understanding.png");


c5 = ROOT.TCanvas("c5","c5");
c5.cd();
hPreviousPerformance.Draw();
c5.SaveAs("PreviousPerformance.png");
'''




c1=ROOT.TCanvas("c1","c1")
c1.cd();
hAttendanceN.Draw()
c1.SaveAs("AttendanceN.png");


c2=ROOT.TCanvas("c2","c2")
c2.cd();
hAlertnessN.Draw()
c2.SaveAs("AlertnessN.png");


c3=ROOT.TCanvas("c3","c3")
c3.cd();
hHomeworkN.Draw()
c3.SaveAs("HomeworkN.png");


c4=ROOT.TCanvas("c4","c4")
c4.cd();
hUnderstandingN.Draw();
c4.SaveAs("UnderstandingN.png");


c5 = ROOT.TCanvas("c5","c5");
c5.cd();
hPreviousPerformanceN.Draw();
c5.SaveAs("PreviousPerformanceN.png");



c6 = ROOT.TCanvas("c6","c6");
c6.cd();
hPerformance.Draw();
c6.SaveAs("PerformanceN.png");


