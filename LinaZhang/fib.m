i = 0;
x = 1;
sum1 = [];
sum2 = [];
if i <= 4000000
    while i <= 4000000
    i = i + x;
    sum1 = [sum1 i] ;    
    x = x + i;
    sum2 = [sum2 x];
    end

end
s1 = [];
s2 = [];
for i=1:length(sum1)
    if rem(sum1(i), 2) == 0
        s1 = [s1 sum1(i)];
    end
end

for j=1:length(sum2)
    if rem(sum2(j), 2) == 0
        s2 = [s2 sum2(j)];
    end
end

sumEvens = 0;
sumEvens = sum(s1) + sum(s2);
disp("TOTAL SUM:")
disp(sumEvens)