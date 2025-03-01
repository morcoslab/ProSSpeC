input_fasta = "/home/ceziegler/Documents/NIA_files/compiled20240222_enzymes_extended_WT.fasta";
normal = load("c4_concat_dca.mat");
scramble = load("c4_manualsub_scramble_DCAparams.mat");
normal_target = FastaHamiltonianTARGET(input_fasta, normal.couplings,normal.H,1,233,1,[]);
scrambled_target = FastaHamiltonianTARGET(input_fasta,scramble.couplings,scramble.H,1,233,1,[]);
target_specH = normal_target - scrambled_target;


