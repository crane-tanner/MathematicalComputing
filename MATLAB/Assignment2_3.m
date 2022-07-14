%% Part 3: Solve linear system of Equations Ax=b 
% 
% A = [1 1; 1 2; 1 3];
% b = [1; 5; 10];
% 
% x = A\b;
% disp(x); 



%Doesn't equal b when calculating Ax. Solution doesn't exist per graph.
x = linspace(-10,10,100);
y1 = 1 - x;
y2 = (1 - x)/2;
y3 = (10-x)/3;

plot(x,y1,x,y2,x,y3);