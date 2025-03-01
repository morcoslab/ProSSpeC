hold on
scram_H =specificity("c4_and_manualsubstrate_scrambled.fasta","c4_concat_dca.mat","c4_manualsub_scramble_DCAparams.mat");
writematrix(scram_H,"c4_and_manualsubstrate_scrambled_specificity.csv")
histogram(scram_H)
histogram(specificity("concat_seqs_peptidaseC4.fasta","c4_concat_dca.mat","c4_manualsub_scramble_DCAparams.mat"))
legend("Scrambled","All Partners")
title("Interaction Hamiltonian")
