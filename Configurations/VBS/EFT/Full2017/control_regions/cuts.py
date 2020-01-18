# cuts

# SUPERCUT #

separator = ' && '

# if there is a clean jet, it must have pt > 30
# if there is not a clean jet, no problem (selections on jets applied next...)
supercut_vector = [     'nLepton>1',
                        'Lepton_pt[0] > 30',
                        'Lepton_pt[1] > 30',    
                        'fabs(Lepton_eta[0]) < 2.5',
                        'fabs(Lepton_eta[1]) < 2.5',                    
                        'Alt$(CleanJet_pt[0],9999.) > 30', 
                        'Alt$(CleanJet_pt[1],9999.) > 30', 
                        'Alt$(fabs(CleanJet_eta[0]),-9999.) < 5',
                        'Alt$(fabs(CleanJet_eta[1]),-9999.) < 5',
                  ]

# supercut definition
supercut = separator.join(supercut_vector)     

## 2 lepton categorization

# same sign
ssLep   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) > 0'       # SS generic leptons
ss_ee   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*11'  # double electron
ss_emu  = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 11*13'  # muon & electron
ss_mumu = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == 13*13'  # double muon

# opposite sign
osLep   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) < 0'       # SS generic leptons
os_ee   = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == -11*11'  # double electron
os_emu  = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == -11*13'  # muon & electron
os_mumu = 'Alt$(Lepton_pdgId[0],0.)*Alt$(Lepton_pdgId[1],0.) == -13*13'  # double muon


#############################################
########## DY control phase space ###########
#############################################

cuts['DY_cr']  = { 
   'expr' : osLep,
   # sub categorization
   'categories' : {
         'ee'    : os_ee,
         'emu'   : os_emu,
         'mumu'  : os_mumu,
   }
}

#############################################
########## top control phase space ##########
#############################################

top =       '\
            nCleanJet >= 2 \
            && detajj > 1.\
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && Lepton_pt[0]>50 \
            && Lepton_pt[1]>40 \
            && CleanJet_pt[0] > 40 \
            && CleanJet_pt[1] > 30 \
            '

cuts['topcr'] = {
   'expr' : top,
   # sub categorization
   'categories' : {
         'ee'    : os_ee,
         'emu'   : os_emu,
         'mumu'  : os_mumu,
   }
}
  

#############################################
########## SS control phase space ##########
#############################################

cuts['SS_cr']  = { 
   'expr' : ssLep,
   # sub categorization
   'categories' : {
         'ee'    : ss_ee,
         'emu'   : ss_emu,
         'mumu'  : ss_mumu,
   }
}



