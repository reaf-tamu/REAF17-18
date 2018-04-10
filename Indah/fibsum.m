fib=1;
fibp=0;
total=0;

while fib<=4000000
   if mod(fib,2)==0
       total=total+fib;
   end
   
   x=fib;
   fib=fib+fibp;
   fibp=x;
end

disp(total);