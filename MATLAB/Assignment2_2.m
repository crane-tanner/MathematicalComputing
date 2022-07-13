%% Part 2: Solving Linear System of Equations Ax = b

A = [ 1 1 1; 1 2 3; 1 3 6];
b = [1; -5; 2];
x = inv(A)*b; 

disp(x);

