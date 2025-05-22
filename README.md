
<img src="img/ProSSpeC_logo.png" alt="ProSSpeC logo. Shows a pickaxe made of DNA hitting an enzyme-substrate complex, where the substrate is colored gold" width="300">

# ProSSpeC - Protease Substrate Specificity Calculator
NIa Protease specificity modeling where Direct Coupling Analysis (DCA) is used to learn couplings and local fields, which are then used to calculate the Hamiltonian specificity between proteases and substrates. An associated web app to run these calculations is available on [https://www.coevolutionary.org/prosspec/](http://www.coevolutionary.org/prosspec/). 

**dca.m** is used to calculate direct information (DI) values \
**DCAparameters.m** is used to calculate the local fields (h<sub>i</sub>) and couplings (e<sub>ij</sub>) \
**FastaHamiltonianT.m** is used to calculate the raw Hamiltonian values. \
**FastaHamiltonianTARGET.m** is used to calculate the raw Hamiltonian values for masked sequences. \
**specificity.m** is used to construct the Hamiltonian specificity. 

## To run:
Install Matlab (test on 2024a) and HMMER (v3.4). (Takes less than 10 minutes) \
Download DCA.zip files from 10.5281/zenodo.15039890 \
Run specificy.m using the unzipped parameters from DCA.zip on a protein sequence fasta. \
The protein sequence fasta must be first aligned to the protease and substrates. Use HMMER and the files from HMM.zip in Zenodo to perform the alignments. The concatenate the protease and substrate (in that order).

**Note: We recommend using the webserver as it performs the alignments and calculations for you.**
## Demo:
1) Download files from Zenodo \
2) Unzip DCA.zip and move parameter files into \demo \
```
unzip DCA.zip
mv *.mat ProSSpec/demo
```
3) Run via matlab from command line
```
matlab -nodisplay -nosplash -r "cd('matlab scripts'); disp(specificity('../demo/demo.fasta', '../demo/concatenated_sequences_DCAparams.mat', '../demo/scrambled_sequences_DCAparams.mat')); exit"
```

## To cite:
Identification and engineering of highly active Potyviral proteases using co-evolutionary models.
Medel B. Lim Suan Jr., Cheyenne Ziegler, Zain Syed, Ajay Tunikipati, Rodrigo Raposo, Jaimahesh Nagineni,
Jaideep Kaur, Faruck Morcos, and P. C. Dave P. Dingal
