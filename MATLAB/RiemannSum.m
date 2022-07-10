% Riemann Sum f(x) = sin(x) 
%% Variables 
N = 1000; 
sum(1) = 0; % holds the sum
%% Code 
for i = 1:N 
    sum(i+1) = sum(i) + sin(i/100)*(1/100);
end

disp(sum(i+1));