% Riemann Sum f(x)
%% Variables 
N = 100; % number of iterations
sum = 0; % holds the sum
%% Code 
for i = 1:N 
    sum(i+1) = sum(i) + sin(i/100)*(1/100);
end

disp(sum);