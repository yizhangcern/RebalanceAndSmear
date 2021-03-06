diempt = 'sqrt(pow(Electrons[0].Px()+Electrons[1].Px(),2)+pow(Electrons[0].Py()+Electrons[1].Py(),2))'
dimupt = 'sqrt(pow(Muons[0].Px()+Muons[1].Px(),2)+pow(Muons[0].Py()+Muons[1].Py(),2))'
diemmass = 'sqrt(pow(Electrons[0].P()+Electrons[1].P(),2)-pow(Electrons[0].Px()+Electrons[1].Px(),2)-pow(Electrons[0].Py()+Electrons[1].Py(),2)-pow(Electrons[0].Pz()+Electrons[1].Pz(),2))'
dimumass = 'sqrt(pow(Muons[0].P()+Muons[1].P(),2)-pow(Muons[0].Px()+Muons[1].Px(),2)-pow(Muons[0].Py()+Muons[1].Py(),2)-pow(Muons[0].Pz()+Muons[1].Pz(),2))'


triggerIndecesV14 = {}
triggerIndecesV14['SingleEl'] = [19]
triggerIndecesV14['SingleEl45'] = [21]
triggerIndecesV14['SingleElCocktail'] = [11,12,14,15,16,18,19,20,21,22,63,64,65]
triggerIndecesV14['MhtMet6pack'] = [56,53,54,55,60,57,58,59]
triggerIndecesV14["SingleMu"] = [23,24,25,26,27]
triggerIndecesV14["SingleMuCocktail"] = [23,24,25,26,27,28,29,30,31,32]
triggerIndecesV14["SinglePho"] = [63]
triggerIndecesV14["SinglePhoWithHt"] = [63,64,65,66]
triggerIndecesV14['HtTrain'] = [38,39,42,43,45,47,48,50,51,52]

triggerIndecesV15 = {}
triggerIndecesV15['SingleEl'] = [36,39]
triggerIndecesV15['SingleEl45'] = [41]
triggerIndecesV15['SingleElCocktail'] = [21,22,23,24,26,27,30,31,32,33,36,37,40,139]
triggerIndecesV15['MhtMet6pack'] = [108,110,114,123,124,125,126,128,129,130,131,132,133,122,134]#123
triggerIndecesV15["SingleMu"] = [48,50,52,55,63]
triggerIndecesV15["SingleMuCocktail"] = [45,46,47,48,49,50,51,52,54,55,58,59,63,64,65,66]
triggerIndecesV15["SinglePho"] = [139]
triggerIndecesV15["SinglePhoWithHt"] = [138, 139,141,142,143]
triggerIndecesV15['HtTrain'] = [67,68,69,72,73,74,80,84,88,91,92,93,95,96,99,102,103,104]

triggerIndecesV16a = triggerIndecesV15

triggerIndecesV16 = {}
triggerIndecesV16['SingleEl'] = [36,39]
triggerIndecesV16['SingleEl45'] = [41]
triggerIndecesV16['SingleElCocktail'] = [21,22,23,24,26,27,30,31,32,33,36,37,40,139]
triggerIndecesV16['MhtMet6pack'] = [108,110,114,123,124,125,126,128,129,130,131,132,133,122,134]#123
triggerIndecesV16["SingleMu"] = [48,50,52,55,63]
triggerIndecesV16["SingleMuCocktail"] = [45,46,47,48,49,50,51,52,54,55,58,59,63,64,65,66]
triggerIndecesV16["SinglePho"] = [139]
triggerIndecesV16["SinglePhoWithHt"] = [138, 139,141,142,143]
triggerIndecesV16['HtTrain'] = [67,68,69,72,73,74,80,84,88,91,92,93,95,96,99,102,103,104]


triggerIndecesV16 = triggerIndecesV16a #this was not yet checked

regionCuts = {}
pi = 3.14159
Inf = 9999
#varlist =                           ['Ht',    'Mht',    'NJets','BTags','SearchBins','MaxDPhi', 'MinDeltaPhiHem','HtRatio']]
regionCuts['Baseline']          = (0,[[300,Inf],[300,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,Inf],      [0,Inf]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LowMhtBaseline']    = (0,[[300,Inf],[250,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,Inf],      [0,2]],  [[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LowMhtSideband']    = (0,[[300,Inf],[250,300],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,Inf],      [0,2]],  [[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
#regionCuts['LowDeltaPhi']       = (1,[[300,Inf],[300,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,Inf],      [0,2]],  [[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LdpLmhtBase']       = (1,[[300,Inf],[250,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,Inf],      [0,2]],  [[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LdpLmhtSideband']   = (1,[[300,Inf],[250,300],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,Inf],      [0,2]],  [[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])

#regionCuts['LowMhtBaseHemv15']  = (0,[[300,Inf],[200,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,15],      [0,2]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
#regionCuts['LdpLmhtBaseHemv15'] = (1,[[300,Inf],[250,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,15],      [0,Inf]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LowMhtBaseHemv0p5']  = (0,[[300,Inf],[250,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0.5,Inf],   [0,2]],  [[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LdpLmhtBaseHemv0p5'] = (1,[[300,Inf],[250,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0.5,Inf],   [0,2]],  [[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])

regionCuts['LowMhtBaseHemv1p0']  = (0,[[300,Inf],[250,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [1.0,Inf],   [0,2]],  [[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LdpLmhtBaseHemv1p0'] = (1,[[300,Inf],[250,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [1.0,Inf],   [0,2]],  [[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])

regionCuts['LowMhtSidebandHemv0p5']  = (0,[[300,Inf],[250,300],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf], [0.5,Inf],      [0,2]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LdpLmhtSidebandHemv0p5'] = (1,[[300,Inf],[250,300],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf], [0.5,Inf],      [0,2]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])

regionCuts['LowMhtSidebandHemv1p0']  = (0,[[300,Inf],[250,300],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf], [1.0,Inf],      [0,2]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LdpLmhtSidebandHemv1p0'] = (1,[[300,Inf],[250,300],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf], [1.0,Inf],      [0,2]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
#regionCuts['LowHtLowDeltaPhi']  = (1,[[300,800],[250,300],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,Inf],      [0,Inf]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
#regionCuts['HighHtLowDeltaPhi'] = (1,[[800,Inf],[250,300],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,Inf],      [0,Inf]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])

'''
regionCuts['BaselineHtr']       = (0,[[300,Inf],[300,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,Inf],      [0,1.3]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LowMhtBaseFpt']     = (0,[[300,Inf],[200,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,100],      [0,2]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LowMhtBaseHtr']     = (0,[[300,Inf],[200,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,Inf],      [0,1.3]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LowMhtBaseFptHtr']  = (0,[[300,Inf],[200,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,100],      [0,1.3]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LowDPhiFptHtr']     = (1,[[300,Inf],[250,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,100],      [0,1.3]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LowDPhiHtr']        = (1,[[300,Inf],[250,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,Inf],      [0,1.3]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])
regionCuts['LowDPhiFpt']        = (1,[[300,Inf],[250,Inf],[2,Inf],[0,Inf],[-Inf, Inf],[0,Inf],    [0,100],      [0,2]],[[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]])


#regionCuts['LowDeltaPhiCR']               = [[1000,Inf],[250,300],[2,Inf],[0,Inf],[0,Inf],[0,Inf],[0,Inf],[0,Inf]]#gets help
#regionCuts['B1Baseline']               = [[300,Inf],[300,Inf],[2,Inf],[1,Inf],[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]]
#regionCuts['LowMhtBaseline']            = ([[300,Inf],[200,Inf],[2,Inf],[0,Inf],[0.0,Inf],[0.0,Inf],[0.0,Inf],[0.0,Inf]], 0)
#regionCuts['HighHtBaseline']               = [[2000,Inf],[300,Inf],[2,Inf],[0,Inf],[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]]
#regionCuts['BaselineBTags0']         = [[300,Inf],[300,Inf],[2,Inf],[0,0],[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]]
#regionCuts['BaselineBTags1']         = [[300,Inf],[300,Inf],[2,Inf],[1,1],[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]]
#regionCuts['BaselineBTags2-Inf']     = [[300,Inf],[300,Inf],[2,Inf],[2,Inf],[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]]
#regionCuts['LowMhtBaseline']            = [[500,Inf],[50,200],[4,Inf],[0,Inf],[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]]
#regionCuts['HighMhtBaseline']               = [[500,Inf],[300,Inf],[2,Inf],[0,Inf],[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]]
#regionCuts['GmsbBaseline']               = [[500,Inf],[100,Inf],[2,Inf],[0,Inf],[0.5,Inf],[0.5,Inf],[0.3,Inf],[0.3,Inf]]#photon
'''

binning = {}
binning['Mht']=[400,0,2000]
binning['Met']=binning['Mht']
binning['Ht']=[50,0,2500]
binning['NJets']=[14,0,14]
binning['BTags']=[0,1,2,3,4,5,6,7]
binning['Jet1Pt']=[50,0,800]
binning['Jet1Eta']=[30,-3,3]
binning['Jet2Pt']=[50,0,800]
binning['Jet2Eta']=[30,-3,3]
binning['Jet3Pt']=[50,0,800]
binning['Jet3Eta']=[30,-3,3]
binning['Jet4Pt']=[50,0,800]
binning['Jet4Eta']=[30,-3,3]
binning['MhtPhi']=[16,0,3.2]
binning['DPhi1']=[16,0,3.2]
binning['DPhi2']=[16,0,3.2]
binning['DPhi3']=[16,0,3.2]
binning['DPhi4']=[16,0,3.2]
binning['SearchBins']=[176,0,176]
binning['MvaLowMht']=[240,-1.2,1.2]
binning['MvaLowHt']=[140,-1.2,1.2]
binning['2015 search bins_RplusS'] = [72,1,73]
binning['2016 search bins_RplusS'] = [174,1,175]
binning['Odd'] = [2,0,2]
binning['csvAve']=[20,0,1]
binning['BestDijetMass']=[30,0,4500]
binning['MinDeltaM']=[30,0,3]
binning['MaxDPhi']=[32,0,3.2]
binning['MaxForwardPt']=[30,20,320]
binning['MaxHemJetPt']=[20,0,100]
binning['HtRatio']=[30,1,4]
binning['MinDeltaPhiHem'] = [32,0,3.2]

'''
binningTemplate = {}
binningTemplate['Mht']=[300,0,600]
binningTemplate['Mht']=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,155,160,165,170,175,180,185,190,195,200,220,240,260,280,300,400,500,800]
binningTemplate['Met']=binningTemplate['Mht']
binningTemplate['Ht']=[0,300,500,700,1000,1500,2000,10000]
binningTemplate['Ht']=[0,200,300,500,700,1000,1500,2000,10000]#NOV2016 removed "400"
binningTemplate['NJets']=[10,0,10]
binningTemplate['BTags']=[0,1,2,5]
binningTemplate['Jet1Pt']=[20,0,800]
binningTemplate['Jet1Eta']=[20,-3,3]
binningTemplate['Jet2Pt']=[20,0,800]
binningTemplate['Jet2Eta']=[20,-3,3]
binningTemplate['Jet3Pt']=[20,0,800]
binningTemplate['Jet3Eta']=[20,-3,3]
binningTemplate['Jet4Pt']=[20,0,800]
binningTemplate['Jet4Eta']=[20,-3,3]
binningTemplate['DPhi1']=[126,0,3.15]
#binningTemplate['DPhi1']=[126,-3.15,3.15]
binningTemplate['DPhi2']=binningTemplate['DPhi1']
binningTemplate['DPhi3']=binningTemplate['DPhi1']
binningTemplate['DPhi4']=binningTemplate['DPhi1']
binningTemplate['MaxForwardPt'] = binning['MaxForwardPt']
binningTemplate['MaxHemJetPt']=[20,0,100]
binningTemplate['HtRatio']=binning['HtRatio']
binningTemplate['MinDeltaPhiHem'] = binning['MinDeltaPhiHem']
'''

binningAnalysis = {}#
binningAnalysis['Mht']=[250,300,350,600,850,2000]
#binningAnalysis['Mht']=[250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,1050,1100,1150,1200,1250,1300,1350,1400,1450,1500,1550,1600,1650,1700,1750,1800,1850,1900,1950,2000]
#inningAnalysis['Mht']=[250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000]
binningAnalysis['Met']=binningAnalysis['Mht']#
binningAnalysis['Ht']=[300,350,600, 850,1200,1700,3000]#
binningAnalysis['NJets']=[2,4,6,8,10,15]#
binningAnalysis['BTags']=[0,1,2,3,10]#
binningAnalysis['Jet1Pt']=[20,0,800]#
binningAnalysis['Jet1Eta']=[20,-3,3]#
binningAnalysis['Jet2Pt']=[20,0,800]#
binningAnalysis['Jet2Eta']=[20,-3,3]#
binningAnalysis['Jet3Pt']=[20,0,800]#
binningAnalysis['Jet3Eta']=[20,-3,3]#
binningAnalysis['Jet4Pt']=[20,0,800]#
binningAnalysis['Jet4Eta']=[20,-3,3]#
binningAnalysis['MhtPhi']=[16,0,3.2]
binningAnalysis['DPhi1']=[16,0,3.2]
binningAnalysis['DPhi2']=[16,0,3.2]
binningAnalysis['DPhi3']=[16,0,3.2]
binningAnalysis['DPhi4']=[16,0,3.2]
binningAnalysis['Odd'] = [2,0,2]
binningAnalysis['SearchBins']=[174,1,175]#174 bins, really check this
binningAnalysis['MvaLowHt']=[5,-1,1]
binningAnalysis['MvaLowMht']=[52,-1.04,1.04]
binningAnalysis['csvAve']=[20,0,1]
binningAnalysis['BestDijetMass']=binning['BestDijetMass']
binningAnalysis['MinDeltaM']=binning['MinDeltaM']
binningAnalysis['MaxDPhi']=binning['MaxDPhi']
binningAnalysis['MaxForwardPt'] = binning['MaxForwardPt']
binningAnalysis['MaxHemJetPt']=binning['MaxHemJetPt']
binningAnalysis['HtRatio']=binning['HtRatio']
binningAnalysis['MinDeltaPhiHem'] = [32,0,3.2]

binning2d = {}
binning2d['Mht']=[0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,340,380,420,460,500,550,600]
binning2d['Met']=binning2d['Mht']
binning2d['Ht']=[0,100,200,300,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000]
binning2d['NJets']=[6,2,14]
binning2d['BTags']=[6,0,6]
binning2d['Jet1Pt']=[60,0,2000]
binning2d['Jet1Eta']=[40,-3,3]
binning2d['Jet2Pt']=[40,0,800]
binning2d['Jet2Eta']=[40,-3,3]
binning2d['Jet3Pt']=[40,0,800]
binning2d['Jet3Eta']=[40,-3,3]
binning2d['Jet4Pt']=[40,0,800]
binning2d['Jet4Eta']=[40,-3,3]
binning2d['MhtPhi']=[16,0,3.2]
binning2d['DPhi1']=[16,0,3.2]
binning2d['DPhi2']=[16,0,3.2]
binning2d['DPhi3']=[16,0,3.2]
binning2d['DPhi4']=[16,0,3.2]
binning2d['Odd'] = [2,0,2]
binning2d['HtRatio']=binning['HtRatio']

binningTemplate = {}
binningTemplate['Mht']=[300,0,600]
binningTemplate['Mht']=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,136,138,140,142,144,146,148,150,155,160,165,170,175,180,185,190,195,200,220,240,260,280,300,400,500,800]
binningTemplate['Met']=binningTemplate['Mht']
binningTemplate['Ht']=[0,300,500,700,1000,1500,2000,10000]
binningTemplate['Ht']=[0,200,300,500,700,1000,1500,2000,10000]#NOV2016 removed "400"
binningTemplate['NJets']=[10,0,10]
binningTemplate['BTags']=[0,1,2,5]
binningTemplate['Jet1Pt']=[20,0,800]
binningTemplate['Jet1Eta']=[20,-3,3]
binningTemplate['Jet2Pt']=[20,0,800]
binningTemplate['Jet2Eta']=[20,-3,3]
binningTemplate['Jet3Pt']=[20,0,800]
binningTemplate['Jet3Eta']=[20,-3,3]
binningTemplate['Jet4Pt']=[20,0,800]
binningTemplate['Jet4Eta']=[20,-3,3]
binningTemplate['DPhi1']=[126,0,3.15]
binningTemplate['DPhi2']=binningTemplate['DPhi1']
binningTemplate['DPhi3']=binningTemplate['DPhi1']
binningTemplate['DPhi4']=binningTemplate['DPhi1']
binningTemplate['HtRatio']=binning['HtRatio']
binningTemplate['MinDeltaPhiHem'] = binning['MinDeltaPhiHem']


binningTrigger = {}
binningTrigger['MHT']=[100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,350,380,410,450,500,600,1000]
binningTrigger['MHTclean']=binningTrigger['MHT']
binningTrigger['HT']=[7,0,2100]
binningTrigger['HTclean']=[7,0,2100]
binningTrigger['Electrons[0].Pt()']=[20,0,500]
binningTrigger['Muons[0].Pt()']=[20,0,500]
binningTrigger['Photons[0].Pt()']=binningTrigger['MHT']
binningTrigger['NJets']=[10,1,11]
binningTrigger[diempt] = binningTrigger['MHT']
binningTrigger[dimupt] = binningTrigger['MHT']
binningTrigger['Photons_hadTowOverEM[0]'] = [20,0,0.05]
binningTrigger['Photons_sigmaIetaIeta[0]'] = [20,0,0.015]
binningTrigger['HtRatio']=binning['HtRatio']
binningTrigger = binning['MinDeltaPhiHem']


binningUser = {}#
binningUser['Mht']=[60,0,1200]#
binningUser['Mht']=[50,200,1200]#
binningUser['Mht']=[20,250,1250]#
#binningUser['Mht']=[0,50,100,150,200,250,300,350,400,450,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,2000]#good
#binningUser['Mht']=[0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,300,500,800,1500,2000]#
#binningUser['Mht']=[55,100,1200]
binningUser['Met']=binningUser['Mht']#
binningUser['Ht']=[10,100,2100]
binningUser['Ht']=[20,100,2100]
#binningUser['Ht']=[60,0,3000]#
binningUser['NJets']=[9,2,11]#
binningUser['BTags']=[4,0,4]#
binningUser['DPhi1']=[16,0,3.2]
binningUser['DPhi2']=[16,0,3.2]
binningUser['DPhi3']=[16,0,3.2]
binningUser['DPhi4']=[16,0,3.2]
binningUser['Jet1Pt']=binning['Jet1Pt']
binningUser['Jet1Eta']=binning['Jet1Eta']
binningUser['Jet2Pt']=binning['Jet2Pt']
binningUser['Jet2Eta']=binning['Jet2Eta']
binningUser['Jet3Pt']=binning['Jet3Pt']
binningUser['Jet3Eta']=binning['Jet3Eta']
binningUser['Jet4Pt']=binning['Jet4Pt']
binningUser['Jet4Eta']=binning['Jet4Eta']
binningUser['MhtPhi']=[16,0,3.2]
binningUser['SearchBins']=[174,1,175]#[72,1,73]#[175,-1,174]#[174,1,175]#174 bins, really check this #[72,1,73]
binningUser['MvaLowMht']=[52,-1.04,1.04]
binningUser['2015 search bins_RplusS'] = [72,1,73]
binningUser['2016 search bins_RplusS'] = [174,1,175]#scootch this up one to be like the above
binningUser['Odd'] = [2,0,2]
binningUser['MvaLowHt']=[5,-1,1]
binningUser['csvAve']=[20,0,1]
binningUser['BestDijetMass']=binning['BestDijetMass']
binningUser['MinDeltaM']=binning['MinDeltaM']
binningUser['MaxDPhi']=binning['MaxDPhi']
binningUser['MaxForwardPt'] = binning['MaxForwardPt']
binningUser['MaxHemJetPt']=binning['MaxHemJetPt']
binningUser['HtRatio']=binning['HtRatio']
binningUser['MinDeltaPhiHem'] = binning['MinDeltaPhiHem']


