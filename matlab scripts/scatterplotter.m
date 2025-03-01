exp_H = specificity("crosstalk_test_concat.fasta","c4_concat_dca.mat","c4_manualsub_scramble_DCAparams.mat");

exp =readtable("Crosstalk test Dec 2023 - Jan 2024 summary.xlsx");
norm_enz = table2array(exp(1:18,8));
% norm_enz = norm_enz([2,3,4,6,8,9,13,14,17,18,20,22]);
% names= names([2,3,4,6,8,9,13,14,17,18,20,22],1);
cor = corrcoef(exp_H, norm_enz);
colors = repelem(1,18);
cogH =[];
noncogH = [];
cognate = [];
noncog = [];
for i=1:18
    if (strcmp(exp.Prediction_{i},'vs test substrate'))
        noncog =[noncog; norm_enz(i)];
        noncogH = [noncogH; exp_H(i)];
    elseif (strcmp(exp.Prediction_{i},'vs cognate substrate'))
        cognate = [cognate; norm_enz(i)];
        cogH = [cogH; exp_H(i)]
    end
end

names = exp.Enzyme(1:18);

hold on
scatter(cogH, cognate,100,"filled");
scatter(noncogH, noncog,100,"filled");
text(-100,0.55,"Pearson R = "+cor(2))
text(exp_H+5, norm_enz, names);
xlabel("Specificity Hamiltonian");
ylabel("Normalized Enzyme");
legend(["Cognate","Crosstalk"])
title("Specificity Prediction vs. Fluorescence")
