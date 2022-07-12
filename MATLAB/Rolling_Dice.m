%% Variables
n = 100000;

%% Code
for l = 1:n 
i = 0; 
dice1= 0; 
dice2= 0; 
    while dice1 < 6 || dice2 < 6
    dice1 = randi([1 6]);
    dice2 = randi([1 6]); 
    i = i + 1;
    end
    overall_count(l) = i;
end

avg_count = sum(overall_count)/n;
disp(avg_count);