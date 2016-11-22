import os

outputdirname="Raman/SkimmedTuples/V11/"

#outputdirname="Raman/AnalysisTuples_2016DataMC_V5/TTBar/"
inputprefix="--input-dir=root://cmsxrootd.hep.wisc.edu//store/user/khurana/"
cmsswpath="/afs/hep.wisc.edu/cms/khurana/MonoH2016MCProduction/MonoHEfficiency/CMSSW_8_0_11"
exepath="/afs/hep.wisc.edu/cms/khurana/MonoH2016MCProduction/MonoHEfficiency/CMSSW_8_0_11/src/MonoH/MonoHbb/"

fout = open("samplestorun.txt","w")

## 76 samples 

samples='''ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-400_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-500_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-500_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-700_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-500_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-500_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-400_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-700_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-400_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-600_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-600_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-700_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-600_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-700_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-500_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-500_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-500_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-500_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-800_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-800_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-600_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-700_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-800_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-800_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-400_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-400_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-400_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-700_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-700_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-800_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-800_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-800_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1200_MA0-800_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-400_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-400_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-300_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-600_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-600_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-600_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-500_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-500_13TeV-madgraph  
ZJetsToNuNu_HT-400To600_13TeV-madgraph MonoH2016/V2_Base/ZJetsToNuNu_HT-400To600_13TeV-madgraph
ZJetsToNuNu_HT-200To400_13TeV-madgraph MonoH2016/V2_Base/ZJetsToNuNu_HT-200To400_13TeV-madgraph
ZJetsToNuNu_HT-600To800_13TeV-madgraph MonoH2016/V2_Base/ZJetsToNuNu_HT-600To800_13TeV-madgraph
ZJetsToNuNu_HT-1200To2500_13TeV-madgraph MonoH2016/V2_Base/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-800_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1000_MA0-800_13TeV-madgraph
WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8 MonoH2016/V2_Base/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8
WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 MonoH2016/V2_Base/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
ZJetsToNuNu_HT-100To200_13TeV-madgraph MonoH2016/V2_Base/ZJetsToNuNu_HT-100To200_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-500_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1400_MA0-500_13TeV-madgraph
ZJetsToNuNu_HT-800To1200_13TeV-madgraph MonoH2016/V2_Base/ZJetsToNuNu_HT-800To1200_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-400_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-400_13TeV-madgraph
WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 MonoH2016/V2_Base/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1 MonoH2016/V2_Base/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1
TT_TuneCUETP8M1_13TeV-powheg-pythia8 MonoH2016/V2_Base/TT_TuneCUETP8M1_13TeV-powheg-pythia8
WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 MonoH2016/V2_Base/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-800_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-2000_MA0-300_13TeV-madgraph
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-300_13TeV-madgraph
WW_TuneCUETP8M1_13TeV-pythia8 MonoH2016/V2_Base/WW_TuneCUETP8M1_13TeV-pythia8
ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1 MonoH2016/V2_Base/ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1
WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 MonoH2016/V2_Base/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-800_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-1700_MA0-800_13TeV-madgraph
ZZ_TuneCUETP8M1_13TeV-pythia8 MonoH2016/V2_Base/ZZ_TuneCUETP8M1_13TeV-pythia8
ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1 MonoH2016/V2_Base/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1
ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1 MonoH2016/V2_Base/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1
ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8 MonoH2016/V2_Base/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8
ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1 MonoH2016/V2_Base/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1
WZ_TuneCUETP8M1_13TeV-pythia8 MonoH2016/V2_Base/WZ_TuneCUETP8M1_13TeV-pythia8
ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph MonoH2016/V2_Base/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph
WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 MonoH2016/V2_Base/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 MonoH2016/V2_Base/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-500_13TeV-madgraph MonoH2016/V2_Base/ZprimeToA0hToA0chichihbb_2HDM_MZp-2500_MA0-500_13TeV-madgraph
WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8 MonoH2016/V2_Base/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8
MonoHbb_ZpBaryonic_MZp-200_MChi-150_13TeV-madgraph MonoH2016/V2_Base/MonoHbb_ZpBaryonic_MZp-200_MChi-150_13TeV-madgraph

MET MonoH2016/V2/MET'''

fout.write(samples)
fout.close()

## 

def submitjobs(scriptname):
    exepath_new = exepath + scriptname

    f = open('samplestorun.txt','r')
    
    for line in f:
        a,b = line.split()
        datasetdet=[a,b]
        jobcommand = ("farmoutAnalysisJobs "+outputdirname+"/"+datasetdet[0]+" "+inputprefix+datasetdet[1]+" "+cmsswpath+" "+exepath_new+" --fwklite --input-files-per-job=15 --extra-inputs=Loader.h")
        
        print "--------------------------------------------------------------"
        print "submitting jobs for"+datasetdet[0]
        print "--------------------------------------------------------------"
        print jobcommand
        os.system(jobcommand)
        



        
#scriptname = 'CopyTree.py'
scriptname = 'SkimTree.py'
submitjobs(scriptname)
