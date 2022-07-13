%% Part 1: Defining the following Matrices and Vectors 
A = [2 -1 4; 9 6 2; 1 3 8];
B = [1 1 1; 1 1 1; 1 1 1];
x = [3;6;8];
y = [5 10 15];

%% Calculations 
calc1 = A*B; 
calc2 = A*x; 
calc3 = x'*B;
%calc4 = B*y; 
%calc5 = x*A; 
calc6 = x*y;
calc7 = y*x; 
%calc8 = x*y'; 
calc9 = x .* y; 
calc10 = A .* B;

%% Display Calculations 
disp(calc1); 
disp(calc2); 
disp(calc3);
%disp(calc4);
% Number of columns in the first matrix must match the number
%of rows in the second matrix.  Cannot Compute
%disp(calc5); Cannot compute for the same reason above
disp(calc6); 
disp(calc7); 
%disp(calc8);
disp(calc9);
disp(calc10); 

%% Part 2: Solving Linear System of Equations Ax = B 

