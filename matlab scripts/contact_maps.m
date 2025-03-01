

dca_contacts = readtable("concatC4_filtered_sorted_interface_only.DI", 'FileType','text');
% for pos=1:height(dca_contacts)
%     dca_contacts(pos,"Var2") = {dca_contacts{pos,"Var2"}-236+300};   
% end
    
structure_contacts = readtable("1lvm_c4_manual_aligned_16", 'FileType','text');
% for pos=1:height(structure_contacts)
%     structure_contacts(pos,"Var1")={structure_contacts{pos,"Var1"}+2};
%     structure_contacts(pos,"Var4")={structure_contacts{pos,"Var4"}+83};
% end
% remove_pos = []
% for pos=1:height(structure_contacts)
%     if structure_contacts{pos,"Var7"}<10 && structure_contacts{pos,"Var1"}<0
%         remove_pos = [remove_pos, pos];
%     end
% end
% structure_contacts(remove_pos,:) = [];

topinterfaceDI = dca_contacts{:,["Var1","Var2"]}(1:20,:);
hits = zeros(length(topinterfaceDI),1);
% Get hits
for i=1:length(topinterfaceDI)
    for j=1:length(structure_interface)
        if topinterfaceDI(i,:) == structure_interface(j,:)
            hits(i) = 1;
        end
    end
end

%Get different sets


structure_interface = structure_contacts{:,:}; % +1 aligns
structure_interface(:,2) = structure_interface(:,2)-300+240;
structure_interface(:,1) = structure_interface(:,1)+2;
plotDCAmap(structure_interface,[],[0 233],0,0,"b")
title("")
