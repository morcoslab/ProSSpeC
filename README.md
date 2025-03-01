# ProSSpeC - Protease Substrate Specificity Calculator
NIa Protease specificity modeling where Direct Coupling Analysis (DCA) is used to learn couplings and local fields, which are then used to calculate the Hamiltonian specificity between proteases and substrates. An associated web app to run these calculations is available on [http://www.coevolutionary.org/prosspec](http://www.coevolutionary.org/prosspec/). 

**dca.m** is used to calculate direct information (DI) values \\
**DCAparameters.m** is used to calculate the local fields (h<sub>i<\sub>) and couplings (e<sub>ij<\sub>) \\
**FastaHamiltonianTARGET.m** is used to calculate the raw Hamiltonian values. \\
**specificity.m** is used to construct the Hamiltonian specificity. \\

## To cite:
Identification and engineering of highly active Potyviral proteases using co-evolutionary models
Medel B. Lim Suan Jr., Cheyenne Ziegler, Zain Syed, Ajay Tunikipati, Rodrigo Raposo, Jaimahesh Nagineni,
Jaideep Kaur, Faruck Morcos, and P. C. Dave P. Dingal
