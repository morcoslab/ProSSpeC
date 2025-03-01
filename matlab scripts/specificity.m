function intH = specificity(fasta, normal_params, scrambled_params)
normal = load(normal_params);
scramble = load(scrambled_params);
total_interface_H = Fastahamiltonian(fasta,normal.couplings,normal.H,1,233,1);
scrambled_H = Fastahamiltonian(fasta,scramble.couplings,scramble.H,1,233,1);
intH = total_interface_H - scrambled_H;
end
