input='full_tevp_msa.afa_filtered20';
output='filt20_extended_dca';
% dca(input,output)

native = readmatrix("1lvm_AE_10");
activesite = readmatrix("1lvm_allatom_AC_10A");
di = readmatrix("filt20_autoinhib");

di_active = []
for item = 1:50
    for active = 1:length(activesite)
        if di(item,1) == activesite(active,1)
            di_active = [di_active; di(item,1:2)];
        end
    end
end
x = plotDCAmap([],native(:,1:2),[229 237],0,0,'black')
y = plotDCAmap(di(1:50,1:2),[],[229 237],0,0,'blue')
z = plotDCAmap(di_active,[], [229 237],0,0,'red')
