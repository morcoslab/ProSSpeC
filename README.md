
<img src="img/ProSSpeC_logo.png" alt="ProSSpeC logo. Shows a pickaxe made of DNA hitting an enzyme-substrate complex, where the substrate is colored gold" width="300">

# ProSSpeC - Protease Substrate Specificity Calculator
NIa Protease specificity modeling where Direct Coupling Analysis (DCA) is used to learn couplings and local fields, which are then used to calculate the Hamiltonian specificity between proteases and substrates. An associated web app to run these calculations is available on [https://www.coevolutionary.org/prosspec/](http://www.coevolutionary.org/prosspec/). 

**dca.m** is used to calculate direct information (DI) values \
**DCAparameters.m** is used to calculate the local fields (h<sub>i</sub>) and couplings (e<sub>ij</sub>) \
**FastaHamiltonianTARGET.m** is used to calculate the raw Hamiltonian values. \
**specificity.m** is used to construct the Hamiltonian specificity. 

## To run:
Download DCA.zip files from 10.5281/zenodo.15039890
Run specificy.m using the unzipped parameters from DCA.zip on a protein sequence fasta.
The protein sequence fasta must be aligned to the protease and substrates. Use hmmer and the files from HMM.zip in Zenodo to perform the alignments. The concatenate the protease and substrate (in that order).
We recommend using the webserver as it performs the alignments and calculations for you.

## To cite:
Identification and engineering of highly active Potyviral proteases using co-evolutionary models.
Medel B. Lim Suan Jr., Cheyenne Ziegler, Zain Syed, Ajay Tunikipati, Rodrigo Raposo, Jaimahesh Nagineni,
Jaideep Kaur, Faruck Morcos, and P. C. Dave P. Dingal
