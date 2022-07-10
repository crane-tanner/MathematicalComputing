%% Variables 
a = 0;
% a < 600 && a > 500 tells to loop when in the range only 
%% Code
while a > 600 || a < 500 % stop when between range of 500 and 600 
a = randi(1000);
disp(a);
end 