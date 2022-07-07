A = [ 2 4; 6 8];
sum = A(1,1) + A(1,2) + A(2,1) + A(2,2)

if (sum>0)
    disp('The sum of the elements are positive!');
elseif (sum < 0)
    disp('The sum of the elements are negative!');
else
   disp('The sum of the elements is 0');
end