load("C:\Users\cheye\Documents\NIA\DCA\c4_concat_dca.mat")

% exp_H = Fastahamiltonian("C:\Users\cheye\Documents\NIA\Sequences\chacha\chacha_concat.fasta", couplings, H,1,236,1);
% exp_H = Fastahamiltonian("C:\Users\cheye\Documents\NIA\Sequences\chacha\c4_aligned_triplicates.fasta", couplings, H,2,233,1);
exp_H = FastahamiltonianInterface("C:\Users\cheye\Documents\NIA\VAE\c4_concat_8x8.fasta", couplings, H,"C:\Users\cheye\Documents\NIA\Structures\RCSB\catalytically_active\1lvm_c4_manual_aligned_16",233,1);
writematrix(exp_H, "C:\Users\cheye\Documents\NIA\VAE\c4_concat_8x8_interface.csv")

% exp =readtable("C:\Users\cheye\Documents\NIA\Complied Data 20230322.xlsx");
% norm_enz = table2array(exp(1:end,9));
% norm_enz = norm_enz([1,5,7,10,11, 12,15,16,19,21,24,25,27]);
% names = exp(1:end,2);
% names= names([1,5,7,10,11, 12,15,16,19,21,24,25,27],1);
% cor = corrcoef(exp_H, norm_enz)
% scatter(exp_H, norm_enz)
% text(-3600,50,"Pearson R = "+cor(2))
% text(exp_H, norm_enz, table2array(names));
% xlabel("Interface Hamiltonian");
% ylabel("Normalized Enzyme");
% title("Interface Hamiltonian Triplicates vs. Fluorescence")

% fam_H = Fastahamiltonian("C:\Users\cheye\Documents\NIA\Sequences\concat_seqs_tevp.fasta", couplings, H,1,236,1);
% hist(fam_H)