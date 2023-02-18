#include<iostream>
#include <TH1.h>
#include "TStyle.h"
#include <TCanvas.h>
#include<Riostream.h>
#include "TROOT.h"
#include<TGraph.h>
#include "TGraphErrors.h"
using namespace std;


void centralLimitTheorem(){


TH1F *h1 = new TH1F("Population", "Population", 100, 0, 100);
h1->GetXaxis()->SetTitle("Observable");
h1->GetYaxis()->SetTitle("Events");



TH1F *hS1 = new TH1F("hS1", "hS1", 100, 0, 100);
hS1->GetXaxis()->SetTitle("Observable");
hS1->GetYaxis()->SetTitle("Events");



TH1F *hS2 = new TH1F("hS2", "hS2", 100, 0, 100);
hS2->GetXaxis()->SetTitle("Observable");
hS2->GetYaxis()->SetTitle("Events");


TH1F *hS3 = new TH1F("hS3", "hS3", 100, 0, 100);
hS3->GetXaxis()->SetTitle("Observable");
hS3->GetYaxis()->SetTitle("Events");








TRandom3 *rng1 = new TRandom3(1);
TRandom3 *rng2= new TRandom3(2);
TRandom3 *rng3 = new TRandom3(219);
TRandom3 *rng4 = new TRandom3(349);



for(int i=0;i<1000000;i++){
  float value1 = rng1->Gaus(30,4);
  float value2 = 100*rng2->Rndm();
  h1->Fill(value1);
  h1->Fill(value2);

}



TCanvas *c0=new TCanvas("c0","c0");
c0->cd();
h1->Draw();
c0->SaveAs("population.png");


// sample analysis starts from here

TH1F *hSample[10000];
char histname[100];

TCanvas *cN[10000];
char cname[100];


for(int i=0;i<10000;i++){
 sprintf(histname,"Sample_%i",i);
 hSample[i]=new TH1F(histname,histname,100,0,100);
}

int histIter=0;


int NumHistGenerate=900;

int sampleSize = 250;
int numDataPoints = sampleSize*NumHistGenerate;

for(int i=0;i<=numDataPoints;i++){
  
  if(i % sampleSize == 0){
   histIter=histIter+1;
  }

   float s1_value1 = rng3->Gaus(30,4);
   float s1_value2 = 100*rng4->Rndm();  
   hSample[histIter]->Fill(s1_value1);
   hSample[histIter]->Fill(s1_value2);



}


char plotname[100];
for(int i=1;i<=NumHistGenerate;i++){
sprintf(cname,"CName_%i",i);
sprintf(plotname,"SamplePlot_%i.png",i);
//cN[i]=new TCanvas(cname,cname);
//cN[i]->cd();
hS1->Fill(hSample[i]->GetMean());
//hSample[i]->Draw();
//cN[i]->SaveAs(plotname);
//cN[i]->Close();
}




TCanvas *hC1=new TCanvas("Mean of Samples", "Mean of Samples");
hC1->cd();
hS1->Draw();

hC1->SaveAs("MeanOfSamples.png");







}
