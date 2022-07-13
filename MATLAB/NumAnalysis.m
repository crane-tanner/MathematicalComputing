%% variables 
f(1) = 0; 
l = 10; % length of interval 
N= 10; %Numvber of steps
h = 1/N; 


%% Code

for n = 1:N
    f(n+1) = f(n) +h*(n^2+n+1);

end 

x = linspace(0,l,N+1);
plot(x,f);